from .settings import *

INSTALLED_APPS += ["channels", "channels_postgres"]

ASGI_APPLICATION = 'testproject.asgi.application'
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_postgres.core.PostgresChannelLayer',
        'CONFIG': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'postgres',
            'USER': 'postgres',
            'PASSWORD': 'password',
            'HOST': 'db',
            'PORT': '5432',
        },
    },
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'channels_postgres_message', 
        'USER': 'postgres', 
        'PASSWORD': 'password',
        'HOST': 'db', 
        'PORT': '5432',
    }
}
