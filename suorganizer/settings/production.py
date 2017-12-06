# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 12:52:36 2017

@author: user
"""
import os

import dj_database_url

from .base import *

DEBUG = False

TEMPLATE_DEBUG = False

SECRET_KEY = os.environ.get('SECRET_KEY')

#db_from_env = dj_database_url.config()
#DATABASES['default'].update(db_from_env)

MIDDLEWARE = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.BrokenLinkEmailsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
)


DATABASES['default'] =  dj_database_url.config()
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',               
        'NAME': os.environ.get('db_name'),                      
        'USER': os.environ.get('db_user'),
        'PASSWORD': os.environ.get('db_user_password'),
        'HOST': 'safe-dusk-45138.herokuapp.com',
        'PORT': '',
    }
}
'''

ALLOWED_HOSTS = [
    'localhost',
    'safe-dusk-45138.herokuapp.com',]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'