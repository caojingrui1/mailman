FROM openeuler/openeuler:22.03

MAINTAINER TomNewChao<tom_toworld@163.com>

# 1.copy
COPY . /opt
RUN mv /opt/docker-entrypoint.sh /usr/local/bin/
RUN mv /opt/mailman-web-v0.4.4/mailman-web /opt
RUN mv /opt/mailman-web-v0.4.4/mailman-web-data /opt
RUN chmod +x /usr/local/bin/docker-entrypoint.sh

# 2. install
RUN yum update -y && yum install python3 -y && python3 -m ensurepip --default-pip && python3 -m pip install --upgrade pip
RUN yum install postgresql-odbc-devel -y && yum install mysql -y && yum install python3-devel -y && yum install sassc -y
RUN cd /opt/django-allauth-0.51.0 && python3 setup.py install
RUN cd /opt/django-mailman3-v1.3.8 && python3 setup.py install
RUN cd /opt/hyperkitty-v1.3.6 && python3 setup.py install
RUN cd /opt/postorius-1.3.7 && python3 setup.py install
RUN pip3 install -r /opt/requirements.txt

# 3.clean
RUN rm -rf /opt/docker-entrypoint.sh && rm -rf /opt/Dockerfile && rm -rf /opt/README && rm -rf /opt/requirements.txt
RUN rm -rf /opt/django-mailman3-v1.3.8 && rm -rf /opt/hyperkitty-v1.3.6 && rm -rf /opt/postorius-1.3.7 && rm -rf /opt/mailman-web-v0.4.4 && rm -rf /opt/django-allauth-0.51.0

# 4. setting
WORKDIR /opt/mailman-web
RUN useradd mailman -s /sbin/nologin -M
RUN mkdir -p /opt/mailman-web-data/logs/
RUN chown -R mailman /opt/ && chmod u+x /opt/mailman-web/manage.py && chmod u+x /opt/mailman-web/uwsgi.ini
EXPOSE 8000 8080
STOPSIGNAL SIGINT

ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["uwsgi", "--ini", "/opt/mailman-web/uwsgi.ini"]