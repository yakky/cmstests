# -*- coding: utf-8 -*-
from __future__ import print_function, division, absolute_import, unicode_literals

import os

from django.core.exceptions import ImproperlyConfigured

import dj_database_url
from unipath import Path

gettext = lambda s: s

env = os.environ.get
true_values = ['1', 'true', 'y', 'yes', 1, True]

def require_env(name):
    value = env(name)
    if not value:
        raise ImproperlyConfigured('Missing {} env variable'.format(name))
    return value

DEBUG = env('DJANGO_DEBUG', 'True').lower() in true_values
TEMPLATE_DEBUG = DEBUG
SHOW_DEBUG_TOOLBAR = False

DATABASES = {
    'default': dj_database_url.config(),
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Europe/Zurich'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

STATIC_URL = "/static/"

# Project root
PROJECT_ROOT = Path(__file__).ancestor(2)

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = env('SECRET_KEY', 'DEBUG_SECRET_KEY')
if SECRET_KEY == 'DEBUG_SECRET_KEY' and DEBUG is False:
    raise ImproperlyConfigured('Missing SECRET_KEY env variable')

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #'django.template.loaders.eggs.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.i18n",
    "django.core.context_processors.debug",
    "django.core.context_processors.request",
    "django.core.context_processors.media",
    'django.core.context_processors.csrf',
    "django.core.context_processors.tz",
    "cms.context_processors.media",
    "sekizai.context_processors.sekizai",
    "django.core.context_processors.static",
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
)

ROOT_URLCONF = 'test_dbrgn.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'test_dbrgn.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    PROJECT_ROOT.child('templates'),
)

CMS_TEMPLATES = (
    ('template_1.html', 'Template One'),
    ('template_2.html', 'Template Two'),
)

LANGUAGES = [
    ('en', 'English'),
    ('it', 'Italian'),
]

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Django CMS stuff
    'cms',  # the CMS itself
    'mptt',  # utilities for implementing a modified pre-order traversal tree
    'menus',  # helper for model independent hierarchical website navigation
    'south',  # intelligent schema and data migrations
    'sekizai',  # for javascript and css management
    'django.contrib.admin',  # django-admin

    # Plugins
    'cms.plugins.file',
    'cms.plugins.flash',
    'cms.plugins.googlemap',
    'cms.plugins.text',
    'cms.plugins.link',
    'cms.plugins.picture',
    'cms.plugins.teaser',
    'cms.plugins.video',

    # Other stuff
    'testx'

)
