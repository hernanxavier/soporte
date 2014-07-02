# coding=utf-8
"""
Django settings for helpdesk project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""



# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from unipath import Path

#BASE_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_DIR = Path(__file__).ancestor(3)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^0_y(3e)5n0vsuvl9s+$+c6842_v@iw%7jcarvoocny49k-k2+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',


     #Para hacer combos dinamicos en el admin
    # chained and grouped selects for django forms - https://github.com/digi604/django-smart-selects/
    #'smart_selects',

     #Tema Para administracion Django http://django-suit.readthedocs.org/en/latest/index.html
    'suit',

    # Extensiones de django (trabaja con pygraphviz que dibuja diagramas entidad relación )
    'django_extensions',

    # Sistema de migraciones para Django http://south.readthedocs.org/en/latest/installation.html
    'south',

    # Permisos para Django http://django-guardian.readthedocs.org/en/v1.2/
    'guardian',

    # Aplicacion que ayuda al ordenamiento de los menus http://django-suit.readthedocs.org/en/latest/sortables.html
    'mptt',

    # DJANGO ALLAUTH The Django sites framework is required  http://django-allauth.readthedocs.org/en/latest/#
    #'django.contrib.sites',


    'helpdesk.apps.equipo',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'helpdesk.helpdesk.urls'

WSGI_APPLICATION = 'helpdesk.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'helpdesk',
        'USER': 'xavier',
        'PASSWORD': 'admin',
        'HOST': 'localhost',    # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
        'PORT': '5432',      # Set to empty string for default.
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es-EC'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
