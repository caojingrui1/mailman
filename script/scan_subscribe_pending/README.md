# 背景

​		用户订阅邮件，但是给用户发送邮件失败，导致用户订阅一直在pending状态下，用户无法再次重新订阅，为此设置定时器脚本每天去忽略（discard处理）

## 安装

~~~bash
yum update -y && yum install python3 -y && python3 -m ensurepip --default-pip && python3 -m pip install --upgrade pip
pip3 install mailmanclient
~~~

## 运行

~~~bash
1.设置环境遍历
mailman_url: http://0.0.0.0:8001/3.1/  # mailman-core服务的url
mailman_username: # mailman-core服务的用户名
mailman_password: # mailman-core服务的密码

2.执行脚本
python3 cancel_subscribe_pending.py
~~~

