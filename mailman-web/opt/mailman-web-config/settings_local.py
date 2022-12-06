# -*- coding: utf-8 -*-
# @FileName: settings_local.py
# @Author  : Tom
# @Create: 2022/4/22 14:47

import os
import socket
import ipaddress

DEBUG = False

SITE_ID = 1

FILTER_VHOST = True

TIME_ZONE = "Asia/Shanghai"

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# NOTE: this is the MTA host, we need to update it.
EMAIL_HOST = 'mailman-exim4-service.mail.svc.cluster.local'
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 25

INSTALLED_APPS = [
    'hyperkitty',
    'postorius',
    'django_mailman3',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'django_gravatar',
    'compressor',
    'haystack',
    'django_extensions',
    'django_q',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
]
ALLOWED_HOSTS = [
    "localhost",
    "0.0.0.0",
    "127.0.0.1",
    "43.155.80.73",
    os.environ.get('SERVE_FROM_DOMAIN'),
    os.environ.get('DJANGO_ALLOWED_HOSTS'),
    "mailweb.osinfra.cn",
    "mailweb.tomtoworld.xyz",
    "mailweb.openhetuengine.org"
]
COMPRESS_CSS_HASHING_METHOD = 'content'
