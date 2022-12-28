#! /bin/bash
set -e

function wait_for_postgres () {
	# Check if the postgres database is up and accepting connections before moving forward.
	until psql $DATABASE_URL -c '\l'; do
		>&2 echo "Postgres is unavailable - sleeping"
		sleep 1
	done
	>&2 echo "Postgres is up - continuing"
}

function wait_for_mysql () {
	# Check if MySQL is up and accepting connections.
	HOSTNAME=$(python3 <<EOF
try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse
o = urlparse('$DATABASE_URL')
print(o.hostname)
EOF
)
	until mysqladmin ping --host "$HOSTNAME" --silent; do
		>&2 echo "MySQL is unavailable - sleeping"
		sleep 1
	done
	>&2 echo "MySQL is up - continuing"
}


function check_or_create () {
	# Check if the path exists, if not, create the directory.
	if [[ ! -e dir ]]; then
		echo "$1 does not exist, creating ..."
		mkdir "$1"
	fi
}

# 1.set env
# Check if $SECRET_KEY is defined, if not, bail out.
if [[ ! -v SECRET_KEY ]]; then
	echo "SECRET_KEY is not defined. Aborting."
	exit 1
fi

if [[ ! -v DATABASE_URL ]]; then
	echo "DATABASE_URL is not defined. Using sqlite database..."
	export DATABASE_URL=sqlite://mailmanweb.db
	export DATABASE_TYPE='sqlite'
fi

if [[ "$DATABASE_TYPE" = 'postgres' ]]
then
	wait_for_postgres
elif [[ "$DATABASE_TYPE" = 'mysql' ]]
then
	wait_for_mysql
fi

# Check if we are in the correct directory before running commands.
if [[ ! $(pwd) == '/opt/mailman-web' ]]; then
	echo "Running in the wrong directory...switching to /opt/mailman-web"
	cd /opt/mailman-web
fi

# Check if the logs directory is setup.
if [[ ! -e /opt/mailman-web-data/logs/mailmanweb.log ]]; then
	echo "Creating log file for mailmanweb.log..."
	touch /opt/mailman-web-data/logs/mailmanweb.log
	chown mailman:mailman /opt/mailman-web-data/logs/mailmanweb.log
fi

if [[ ! -e /opt/mailman-web-data/logs/uwsgi.log ]]; then
	echo "Creating log file for uwsgi.log..."
	touch /opt/mailman-web-data/logs/uwsgi.log
	chown mailman:mailman /opt/mailman-web-data/logs/uwsgi.log
fi

if [[ ! -e /opt/mailman-web-data/logs/uwsgi-error.log ]]; then
	echo "Creating log file for uwsgi-error.log..."
	touch /opt/mailman-web-data/logs/uwsgi-error.log
	chown mailman:mailman /opt/mailman-web-data/logs/uwsgi-error.log
fi

if [[ ! -e /opt/mailman-web-data/logs/uwsgi-qcluster.log ]]; then
	echo "Creating log file for uwsgi-qcluster.log..."
	touch /opt/mailman-web-data/logs/uwsgi-qcluster.log
	chown mailman:mailman /opt/mailman-web-data/logs/uwsgi-qcluster.log
fi

if [[ ! -e /opt/mailman-web-data/logs/uwsgi-cron.log ]]; then
	echo "Creating log file for uwsgi-cron.log..."
	touch /opt/mailman-web-data/logs/uwsgi-cron.log
	chown mailman:mailman /opt/mailman-web-data/logs/uwsgi-cron.log
fi

# 2.collect static file and migrate to mysql and create superuser
# Collect static for the django installation.
python3 manage.py collectstatic --noinput
mkdir -p /opt/mailman-web-static/static/CACHE/
chown -R mailman:mailman /opt/mailman-web-static

# Migrate all the data to the database if this is a new installation, otherwise
# this command will upgrade the database.
python3 manage.py migrate

# If MAILMAN_ADMIN_USER and MAILMAN_ADMIN_EMAIL is defined create a new
# superuser for Django. There is no password setup so it can't login yet unless
# the password is reset.
if [[ -v MAILMAN_ADMIN_USER ]] && [[ -v MAILMAN_ADMIN_EMAIL ]];
then
	echo "Creating admin user $MAILMAN_ADMIN_USER ..."
	python3 manage.py createsuperuser --noinput --username "$MAILMAN_ADMIN_USER"\
		   --email "$MAILMAN_ADMIN_EMAIL" 2> /dev/null || \
		echo "Superuser $MAILMAN_ADMIN_USER already exists"
fi

# If SERVE_FROM_DOMAIN is defined then rename the default `example.com`
# domain to the defined domain.
if [[ -v SERVE_FROM_DOMAIN ]];
then
	echo "Setting $SERVE_FROM_DOMAIN as the default domain ..."
	python3 manage.py shell -c \
	"from django.contrib.sites.models import Site; Site.objects.filter(domain='example.com').update(domain='$SERVE_FROM_DOMAIN', name='$SERVE_FROM_DOMAIN')"
fi

# Create a mailman user with the specific UID and GID and do not create home
# directory for it. Also chown the logs directory to write the files.


exec $@
