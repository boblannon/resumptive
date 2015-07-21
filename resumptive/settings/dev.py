from settings.base import *

DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!3993g7^d=zrvl)9bz&gtxnav9c-v6&01_31hjfx@#n8(fg7%4'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'resumptive',
        'USER': 'resumptive-dev',
        'PASSWORD': 'dev',
        'HOST': 'localhost',
        'PORT': '',
    }
}
