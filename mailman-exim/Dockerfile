FROM openeuler/openeuler:latest

MAINTAINER TomNewChao<tom_toworld@163.com>

WORKDIR /root

ENV TINI_VERSION v0.19.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
RUN chmod 755 /usr/bin/tini
RUN yum install git wget rpm-build rpmdevtools dnf-plugins-core -y
RUN cd /root && rpmdev-setuptree
RUN mkdir /root/rpm
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
RUN cd /root && git clone https://gitee.com/src-openeuler/exim.git
RUN cp /root/exim/exim.spec /root/rpmbuild/SPECS/ && cp /root/exim/* /root/rpmbuild/SOURCES/ -r && yum-builddep /root/rpmbuild/SPECS/exim.spec -y
RUN useradd exim -u 93
RUN rpmbuild -ba /root/rpmbuild/SPECS/exim.spec
RUN yum install /root/rpmbuild/RPMS/x86_64/exim-4.96-1.x86_64.rpm -y
RUN rm -rf /root/rpm && rm -rf /root/rpmbuild && rm -rf /root/exim

COPY .. /etc/exim/
COPY email-addresses /etc/email-addresses
RUN cp /usr/sbin/exim /usr/sbin/exim4

