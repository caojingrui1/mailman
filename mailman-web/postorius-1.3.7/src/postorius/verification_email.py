# -*- coding: utf-8 -*-
# @Time    : 2023/1/17 11:29
# @Author  : Tom_zc
# @FileName: verification_email.py
# @Software: PyCharm
import os
import binascii
import json
import logging
from django.core.mail import send_mail
from django.conf import settings
from pyDes import des, CBC, PAD_PKCS5

logger = logging.getLogger(__name__)

Template = '''
<div style="margin:10px 20px;font-size:12px;">
    <div>邮箱退订确认</div>
    <div>Email Address Unsubscribe Confirmation</div>
    <br>
    <div>您好，这是{domain}的邮件列表服务，我们收到来自您的邮箱的退订请求。</div>
    <div>Hello, this is the Mailman server at {domain}. We have received a unsubscribe request for your email address.</div>
    <br>
    <div>你可以通过点击以下链接来进行确认：</div>
    <div>You can click on the link below to Undergo verification:</div>
    <br>
    <div><a href="{link}">{link}</div>
    <br>
    <div>若您不想退订该邮箱，请忽略此消息。</div>
    <div>If you do not wish to register this email address, simply disregard this message.</div>
'''


class DESCrypt:
    secret_key = "23129838"
    iv = "36384698"

    @classmethod
    def encrypt(cls, s):
        k = des(cls.secret_key, CBC, cls.iv, pad=None, padmode=PAD_PKCS5)
        en = k.encrypt(s, padmode=PAD_PKCS5)
        return binascii.b2a_hex(en)

    @classmethod
    def decrypt(cls, s):
        k = des(cls.secret_key, CBC, cls.iv, pad=None, padmode=PAD_PKCS5)
        de = k.decrypt(binascii.a2b_hex(s), padmode=PAD_PKCS5)
        return de


class UnsubscribeEmailLib(object):
    aescrypt = DESCrypt()
    unsubscribe_url = "https://{}/postorius/lists/{}/anonymous_unsubscribe?k={}"

    @classmethod
    def send_message(cls, list_name, templates, recipient_list):
        """use mta to send msg"""
        if not isinstance(recipient_list, list):
            recipient_list = [recipient_list]
        subject = "Your confirmation is needed to leave the {} mailing list".format(list_name)
        from_email = settings.DEFAULT_FROM_EMAIL
        auth_user = settings.EMAIL_HOST_USER
        auth_password = settings.EMAIL_HOST_PASSWORD
        send_mail(subject, None, from_email, recipient_list, auth_user=auth_user, auth_password=auth_password,
                  html_message=templates)

    @classmethod
    def send_email(cls, email, list_id):
        """send the unsubscribe email to user"""
        web_domain = settings.SERVE_WEB_DOMAIN
        # https://mailweb.osinfra.cn/postorius/lists/tom.lists.osinfra.cn/anonymous_subscribe
        save_dict = {
            "email": email,
            "list_id": list_id,
        }
        str_data = json.dumps(save_dict)
        encrypt_text = cls.aescrypt.encrypt(str_data)
        url_data = str(encrypt_text, encoding="utf-8")
        link = cls.unsubscribe_url.format(web_domain, list_id, url_data)
        list_name = list_id.replace(".", "@", 1)
        template = Template.format(
            domain=list_name,
            link=link
        )
        cls.send_message(list_name, template, email)

    @classmethod
    def parse_text(cls, encrypt_text):
        """parse text to obj"""
        encrypt_str = cls.aescrypt.decrypt(bytes(encrypt_text, encoding="utf-8"))
        save_dict = json.loads(encrypt_str)
        return save_dict
