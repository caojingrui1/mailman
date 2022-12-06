FROM openeuler/openeuler:22.03

MAINTAINER TomNewChao<tom_toworld@163.com>

COPY . /opt
RUN mv /opt/docker-entrypoint.sh /usr/local/bin/
RUN chmod +x /usr/local/bin/docker-entrypoint.sh
RUN mv /opt/opt/mailman-web /opt
RUN mv /opt/opt/mailman-web-config /opt
RUN mv /opt/opt/mailman-web-data /opt
RUN mv /opt/opt/summary.html /opt

RUN yum update -y && yum install python3 -y && python3 -m ensurepip --default-pip && python3 -m pip install --upgrade pip
RUN yum install postgresql-odbc-devel -y && yum install mysql -y && yum install python3-devel -y && yum install rubygem-sass -y
RUN pip3 install django_gravatar==0.1.0 && pip3 install django-gravatar2==1.4.4 && pip3 install dj_database_url==1.0.0 && pip3 install uwsgi==2.0.21 && pip3 install pymysql==1.0.2
RUN pip3 install whoosh==2.7.4
# RUN pip3 install mailman-web==0.0.6 && python3 setup.py install
RUN cd /opt/django-mailman3-v1.3.8 && python3 setup.py install
RUN cd /opt/hyperkitty-v1.3.6 && python3 setup.py install
RUN cd /opt/postorius-1.3.7 && python3 setup.py install
RUN pip3 install django==3.2

RUN rm -rf /opt/docker-entrypoint.sh && rm -rf /opt/Dockerfile && rm -rf /opt/README && rm -rf /opt/opt
RUN rm -rf /opt/django-mailman3-v1.3.8 && rm -rf /opt/hyperkitty-v1.3.6 && rm -rf /opt/postorius-1.3.7

WORKDIR /opt/mailman-web
RUN useradd mailman -s /sbin/nologin -M
RUN chown -R mailman /opt/mailman-web/ && chmod u+x /opt/mailman-web/manage.py && chmod u+x /opt/mailman-web/uwsgi.ini

EXPOSE 8000 8080
STOPSIGNAL SIGINT

ENTRYPOINT ["docker-entrypoint.sh"]
CMD ["uwsgi", "--ini", "/opt/mailman-web/uwsgi.ini"]
