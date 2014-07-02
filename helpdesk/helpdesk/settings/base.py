# coding=utf-8

__author__ = 'xavier'

"""
Django settings for helpdesk project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# import os

from unipath import Path

#BASE_DIR = os.path.dirname(os.path.dirname(__file__))
BASE_DIR = Path(__file__).ancestor(3)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^0_y(3e)5n0vsuvl9s+$+c6842_v@iw%7jcarvoocny49k-k2+'


# Application definition

DJANGO_APPS = (

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

THIRD_PARTY_APPS = (
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

)

LOCAL_APPS = (

    'apps.equipo',
)


# Application definition
INSTALLED_APPS = THIRD_PARTY_APPS + DJANGO_APPS + LOCAL_APPS

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'helpdesk.urls'
WSGI_APPLICATION = 'helpdesk.wsgi.application'



# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es-EC'

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Define directorio para los templates
TEMPLATE_DIRS = [BASE_DIR.child('templates'), ]

#Define Directorio para los archivos staticos (css, js, img ...)
STATICFILES_DIRS = [BASE_DIR.child('static'), ]