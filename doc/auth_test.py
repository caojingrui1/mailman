#!/usr/bin/python
# -*- coding: UTF-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header
import sys

# config
sender = 'test@opengauss.org'  # 更换为当前邮件列表的地址
receivers = ["353712216@qq.com"]  # 更改为接收的邮箱
subject = 'hi!This is Tom'
message = MIMEText('Nice to meet you..', 'plain', 'utf-8')
message['Subject'] = Header(subject, 'utf-8')
message['To'] = sender
ip = "43.154.162.238"  # 接受服务的ip
port = 25
ssl_port = 465
username = "****"
password = "*****"


def email_test_1():
    try:
        smtp_obj = smtplib.SMTP(ip, port)
        smtp_obj.sendmail(sender, receivers, message.as_string())
        print("Testing Scenarios: port:25, is_starttls: no, is_logins: no, result: yes")
    except Exception as e:
        print(e)
        print("Testing Scenarios: port:25, is_starttls: no, is_logins: no, result: fault")


def email_test_2():
    try:
        smtp_obj = smtplib.SMTP(ip, port)
        smtp_obj.login(username, password)
        smtp_obj.sendmail(sender, receivers, message.as_string())
        print("Testing Scenarios: port:25, is_starttls: no, is_logins: yes(all is ok), result: yes")
    except Exception as e:
        print(e)
        print("Testing Scenarios: port:25, is_starttls: no, is_logins: yes(all is ok), result: fault")


def email_test_3():
    try:
        smtp_obj = smtplib.SMTP(ip, port)
        smtp_obj.login('adssfdsf', password)
        smtp_obj.sendmail(sender, receivers, message.as_string())
        print("Testing Scenarios: port:25, is_starttls: no, is_logins: yes(fault username), result: yes")
    except Exception as e:
        print(e)
        print("Testing Scenarios: port:25, is_starttls: no, is_logins: yes(fault username), result: fault")


def email_test_4():
    try:
        smtp_obj = smtplib.SMTP(ip, port)
        smtp_obj.login(username, "password")
        smtp_obj.sendmail(sender, receivers, message.as_string())
        print("Testing Scenarios: port:25, is_starttls: no, is_logins: yes(fault password), result: yes")
    except Exception as e:
        print(e)
        print("Testing Scenarios: port:25, is_starttls: no, is_logins: yes(fault password), result: fault")


def email_test_5():
    try:
        smtp_obj = smtplib.SMTP(ip, port)
        smtp_obj.starttls()
        smtp_obj.sendmail(sender, receivers, message.as_string())
        print("Testing Scenarios: port:25, is_starttls: yes, is_logins: no, result: yes")
    except Exception as e:
        print(e)
        print("Testing Scenarios: port:25, is_starttls: yes, is_logins: no, result: fault")


def email_test_6():
    try:
        smtp_obj = smtplib.SMTP(ip, port)
        smtp_obj.starttls()
        smtp_obj.login(username, password)
        smtp_obj.sendmail(sender, receivers, message.as_string())
        print("Testing Scenarios: port:25, is_starttls: yes, is_logins: yes(all is ok), result: yes")
    except Exception as e:
        print(e)
        print("Testing Scenarios: port:25, is_starttls: yes, is_logins: yes(all is ok), result: fault")


def email_test_7():
    try:
        smtp_obj = smtplib.SMTP(ip, port)
        smtp_obj.starttls()
        smtp_obj.login('adssfdsf', password)
        smtp_obj.sendmail(sender, receivers, message.as_string())
        print("Testing Scenarios: port:25, is_starttls: yes, is_logins: yes(fault username), result: yes")
    except Exception as e:
        print(e)
        print("Testing Scenarios: port:25, is_starttls: yes, is_logins: yes(fault username), result: fault")


def email_test_8():
    try:
        smtp_obj = smtplib.SMTP(ip, port)
        smtp_obj.starttls()
        smtp_obj.login(username, "password")
        smtp_obj.sendmail(sender, receivers, message.as_string())
        print("Testing Scenarios: port:25, is_starttls: yes, is_logins: yes(fault password), result: yes")
    except Exception as e:
        print(e)
        print("Testing Scenarios: port:25, is_starttls: yes, is_logins: yes(fault password), result: fault")


def email_test_9():
    try:
        smtp_obj = smtplib.SMTP_SSL(ip, ssl_port)
        smtp_obj.sendmail(sender, receivers, message.as_string())
        print("Testing Scenarios: port:465, is_starttls: no, is_logins: no, result: yes")
    except Exception as e:
        print(e)
        print("Testing Scenarios: port:465, is_starttls: no, is_logins: no, result: fault")


def email_test_10():
    try:
        smtp_obj = smtplib.SMTP_SSL(ip, ssl_port)
        smtp_obj.login(username, password)
        smtp_obj.sendmail(sender, receivers, message.as_string())
        print("Testing Scenarios: port:465, is_starttls: no, is_logins: yes(all is ok), result: yes")
    except Exception as e:
        print(e)
        print("Testing Scenarios: port:465, is_starttls: no, is_logins: yes(all is ok), result: fault")


def email_test_11():
    try:
        smtp_obj = smtplib.SMTP_SSL(ip, ssl_port)
        smtp_obj.login('adssfdsf', password)
        smtp_obj.sendmail(sender, receivers, message.as_string())
        print("Testing Scenarios: port:465, is_starttls: no, is_logins: yes(fault username), result: yes")
    except Exception as e:
        print(e)
        print("Testing Scenarios: port:465, is_starttls: no, is_logins: yes(fault username), result: fault")


def email_test_12():
    try:
        smtp_obj = smtplib.SMTP_SSL(ip, ssl_port)
        smtp_obj.login(username, "password")
        smtp_obj.sendmail(sender, receivers, message.as_string())
        print("Testing Scenarios: port:465, is_starttls: no, is_logins: yes(fault password), result: yes")
    except Exception as e:
        print(e)
        print("Testing Scenarios: port:465, is_starttls: no, is_logins: yes(fault password), result: fault")


def email_test_13():
    try:
        smtp_obj = smtplib.SMTP_SSL(ip, ssl_port)
        smtp_obj.starttls()
        smtp_obj.sendmail(sender, receivers, message.as_string())
        print("Testing Scenarios: port:465, is_starttls: yes, is_logins: no, result: yes")
    except Exception as e:
        print(e)
        print("Testing Scenarios: port:465, is_starttls: yes, is_logins: no, result: fault")


def email_test_14():
    try:
        smtp_obj = smtplib.SMTP_SSL(ip, ssl_port)
        smtp_obj.starttls()
        smtp_obj.login(username, password)
        smtp_obj.sendmail(sender, receivers, message.as_string())
        print("Testing Scenarios: port:465, is_starttls: yes, is_logins: yes(all is ok), result: yes")
    except Exception as e:
        print(e)
        print("Testing Scenarios: port:465, is_starttls: yes, is_logins: yes(all is ok), result: fault")


def email_test_15():
    try:
        smtp_obj = smtplib.SMTP_SSL(ip, ssl_port)
        smtp_obj.starttls()
        smtp_obj.login('adssfdsf', password)
        smtp_obj.sendmail(sender, receivers, message.as_string())
        print("Testing Scenarios: port:465, is_starttls: yes, is_logins: yes(fault username), result: yes")
    except Exception as e:
        print(e)
        print("Testing Scenarios: port:465, is_starttls: yes, is_logins: yes(fault username), result: fault")


def email_test_16():
    try:
        smtp_obj = smtplib.SMTP_SSL(ip, ssl_port)
        smtp_obj.starttls()
        smtp_obj.login(username, "password")
        smtp_obj.sendmail(sender, receivers, message.as_string())
        print("Testing Scenarios: port:465, is_starttls: yes, is_logins: yes(fault password), result: yes")
    except Exception as e:
        print(e)
        print("Testing Scenarios: port:465, is_starttls: yes, is_logins: yes(fault password), result: fault")


def main():
    mod = sys.modules[__name__]
    for attr in mod.__dict__.keys():
        if attr.startswith("email_test_"):
            method = getattr(mod, attr)
            method()


if __name__ == '__main__':
    main()
