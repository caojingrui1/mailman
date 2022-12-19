FROM openeuler/openeuler:latest

MAINTAINER TomNewChao<tom_toworld@163.com>

WORKDIR /root

ENV TINI_VERSION v0.19.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
RUN chmod 755 /usr/bin/tini
RUN yum install wget -y
RUN mkdir /root/rpm
RUN cd /root/rpm && wget http://119.3.219.20:82/openEuler:/Mainline/standard_x86_64/x86_64/exim-4.96-1.oe1.x86_64.rpm
RUN cd /root/rpm && wget http://119.3.219.20:82/openEuler:/Mainline/standard_x86_64/x86_64/libspf2-1.2.11-1.oe1.x86_64.rpm
RUN cd /root/rpm && wget http://119.3.219.20:82/openEuler:/Mainline/standard_x86_64/x86_64/libspf2-devel-1.2.11-1.oe1.x86_64.rpm
RUN cd /root/rpm && wget http://119.3.219.20:82/openEuler:/Mainline/standard_x86_64/x86_64/libopendmarc-1.4.2-1.oe1.x86_64.rpm
RUN cd /root/rpm && wget http://119.3.219.20:82/openEuler:/Mainline/standard_x86_64/x86_64/libopendmarc-devel-1.4.2-1.oe1.x86_64.rpm
RUN cd /root/rpm && wget http://119.3.219.20:82/openEuler:/Mainline/standard_x86_64/x86_64/libbsd-0.10.0-1.oe1.x86_64.rpm
RUN cd /root/rpm && wget http://119.3.219.20:82/openEuler:/Mainline/standard_x86_64/x86_64/libbsd-devel-0.10.0-1.oe1.x86_64.rpm
RUN rpm -ivh /root/rpm/libbsd-0.10.0-1.oe1.x86_64.rpm
RUN rpm -ivh /root/rpm/libbsd-devel-0.10.0-1.oe1.x86_64.rpm
RUN rpm -ivh /root/rpm/libopendmarc-1.4.2-1.oe1.x86_64.rpm
RUN rpm -ivh /root/rpm/libopendmarc-devel-1.4.2-1.oe1.x86_64.rpm
RUN rpm -ivh /root/rpm/libspf2-1.2.11-1.oe1.x86_64.rpm
RUN rpm -ivh /root/rpm/libspf2-devel-1.2.11-1.oe1.x86_64.rpm
RUN yum install /root/rpm/exim-4.96-1.oe1.x86_64.rpm -y

COPY .. /etc/exim/
COPY email-addresses /etc/email-addresses
RUN cp /usr/sbin/exim /usr/sbin/exim4

