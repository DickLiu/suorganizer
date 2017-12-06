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

DATABSES = {
        'default': dj_database_url.config(
                default='sqlite:///{}'.format(
                        os.path.abspath(
                                os.path.join(
                                        BASE_DIR, 'db.sqlite3'))),
                        ),
                        }

ALLOWED_HOSTS = ['*']

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'