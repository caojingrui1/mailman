FROM openeuler/openeuler:23.03

MAINTAINER TomNewChao<tom_toworld@163.com>

WORKDIR /root

ENV TINI_VERSION v0.19.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
RUN chmod 755 /usr/bin/tini
RUN yum install -y libspf2 libspf2-devel libopendmarc libopendmarc-devel libbsd libbsd-devel exim

COPY .. /etc/exim/
COPY email-addresses /etc/email-addresses
RUN cp /usr/sbin/exim /usr/sbin/exim4

