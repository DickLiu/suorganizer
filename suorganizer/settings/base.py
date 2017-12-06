# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 12:51:59 2017

@author: user
"""
import os

from django.core.urlresolvers import reverse_lazy

BASE_DIR = os.path.dirname(
        os.path.dirname(
                os.path.dirname(
                        __file__)))

SITE_ID = 1

INSTALLED_APPS = (
    'user',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'core',
    'organizer',
    'blog',
    'contact',
)

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
    'django.middleware.cache.FetchFromCacheMiddleware',
)

ROOT_URLCONF = 'suorganizer.urls'

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [
        os.path.join(BASE_DIR, 'templates'),
    ],
    'OPTIONS': {
        'context_processors': [
            'django.template.context_processors.debug',
            'django.template.context_processors.request',
            'django.contrib.auth.context_processors.auth',
            'django.contrib.messages.context_processors.messages',
        ],
        'loaders': [
            'django.template.loaders.filesystem.Loader',
            'django.template.loaders.app_directories.Loader',
        ],
    },
}]

WSGI_APPLICATION = 'suorganizer.wsgi.application'

# User
# https://docs.djangoproject.com/en/1.8/topics/auth/customizing/#substituting-a-custom-user-model

AUTH_USER_MODEL = 'user.User'

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/
LANGUAGES = (
        ('en', 'English'),
        ('zh-hant', 'Traditional Chinese'),)

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Login Settings
# https://docs.djangoproject.com/en/1.8/topics/auth/

LOGIN_REDIRECT_URL = reverse_lazy('blog_post_list')
LOGIN_URL = reverse_lazy('dj-auth:login')
LOGOUT_URL = reverse_lazy('dj-auth:logout')

# Email
# https://docs.djangoproject.com/en/1.8/topics/email/

SERVER_EMAIL = 'contact@django-unleashed.com'
DEFAULT_FROM_EMAIL = 'no-reply@django-unleashed.com'
EMAIL_SUBJECT_PREFIX = '[Startup Organizer] '
MANAGERS = (
    ('Us', 'ourselves@django-unleashed.com'),
)

# Fixtures
# https://docs.djangoproject.com/en/1.8/topics/serialization/

FIXTURE_DIRS = (os.path.join(BASE_DIR, 'fixtures'),)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)
STATIC_ROOT = os.path.join(BASE_DIR, 'collected_static')