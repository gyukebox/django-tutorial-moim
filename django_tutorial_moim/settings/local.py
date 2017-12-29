from django_tutorial_moim.settings.base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'moim_db',
        'USER': 'root',
        'PASSWORD': 'biss9541',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}