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
<div style="margin:10px 20px;font-size:16px;">
    <div>Hello from {domain}!</div>
    <div>You're receiving this e-mail because you or someone else has requested a unsubscribe email list for your user account.</div>
    <br>
    <div>Your verification Link is: <a href="{link}">{link}</div>
    <br>
    <div>Thank you for using {domain}!</div>
    <div>{domain}</div>
</div>
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
    def send_message(cls, domain, templates, recipient_list):
        """use mta to send msg"""
        if not isinstance(recipient_list, list):
            recipient_list = [recipient_list]
        subject = "[{}] Unsubscribe Verification Link".format(domain)
        current_host = os.environ.get('SERVE_FROM_DOMAIN', 'localhost.local')
        from_email = "postorius@{}".format(current_host)
        auth_user = settings.EMAIL_HOST_USER
        auth_password = settings.EMAIL_HOST_PASSWORD
        send_mail(subject, None, from_email, recipient_list, auth_user=auth_user, auth_password=auth_password,
                  html_message=templates)

    @classmethod
    def send_email(cls, email, list_id):
        """send the unsubscribe email to user"""
        domain = settings.DEFAULT_FROM_EMAIL.split("@")[-1]
        # https://mailweb.osinfra.cn/postorius/lists/tom.lists.osinfra.cn/anonymous_subscribe
        save_dict = {
            "email": email,
            "list_id": list_id,
        }
        str_data = json.dumps(save_dict)
        encrypt_text = cls.aescrypt.encrypt(str_data)
        url_data = str(encrypt_text, encoding="utf-8")
        link = cls.unsubscribe_url.format(domain, list_id, url_data)
        template = Template.format(
            domain=domain,
            link=link
        )
        cls.send_message(domain, template, email)

    @classmethod
    def parse_text(cls, encrypt_text):
        """parse text to obj"""
        encrypt_str = cls.aescrypt.decrypt(bytes(encrypt_text, encoding="utf-8"))
        save_dict = json.loads(encrypt_str)
        return save_dict
