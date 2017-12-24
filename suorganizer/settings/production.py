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


ALLOWED_HOSTS = [
    'localhost',
    'dry-inlet-24923.herokuapp.com',]

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID", "")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY", "")
AWS_STORAGE_BUCKET_NAME = os.environ.get("AWS_STORAGE_BUCKET_NAME", "")
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"

AWS_QUERYSTRING_AUTH = False 
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATIC_URL = 'https://' + AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com/'
MEDIA_URL = STATIC_URL + 'media/'
ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'


STATICFILES_FINDERS = (
'django.contrib.staticfiles.finders.FileSystemFinder',
'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
'''
def get_cache():
    try:
        os.environ['MEMCACHE_SERVERS'] = os.environ.get('MEMCACHIER_SERVERS', '').replace(',', ';')
        os.environ['MEMCACHE_USERNAME'] = os.environ.get('MEMCACHIER_USERNAME', '')
        os.environ['MEMCACHE_PASSWORD'] = os.environ.get('MEMCACHIER_PASSWORD', '')
        return {        
                'default': {        
                        # Use pylibmc        
                        'BACKEND': 'django_pylibmc.memcached.PyLibMCCache',        
                        # Use binary memcache protocol (needed for authentication)        
                        'BINARY': True,        
                        # TIMEOUT is not the connection timeout! It's the default expiration        
                        # timeout that should be applied to keys! Setting it to `None`        
                        # disables expiration.        
                        'TIMEOUT': None,        
                        'OPTIONS': {            
                                # Enable faster IO            
                                'tcp_nodelay': True,            
                                # Keep connection alive            
                                'tcp_keepalive': True,            
                                # Timeout settings            
                                'connect_timeout': 2000, # ms            
                                'send_timeout': 750 * 1000, # us            
                                'receive_timeout': 750 * 1000, # us            
                                '_poll_timeout': 2000, # ms            
                                
                                # Better failover            
                                'ketama': True,            
                                'remove_failed': 1,            
                                'retry_timeout': 2,            
                                'dead_timeout': 30,
        }
    }
}
    except:
        return {
        'default': {
        'BACKEND': 
            'django.core.cache.backends.locmem.LocMemCache'
            }
        }
CACHES = get_cache()
'''
