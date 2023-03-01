FROM openeuler/openeuler:22.03

MAINTAINER TomNewChao<tom_toworld@163.com>

# 1.copy
COPY . /opt
RUN chmod +x /opt/cancel_subscribe_pending.py

# 2. install
RUN yum update -y && yum install python3 -y && python3 -m ensurepip --default-pip && python3 -m pip install --upgrade pip
RUN pip3 install mailmanclient

CMD ["python3", "/opt/cancel_subscribe_pending.py"]