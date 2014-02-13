from .settings import *

TEMPLATE_DEBUG = DEBUG = False

ALLOWED_HOSTS = [
    'demo.wid.gy',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'widgy_demo',
        'USER': 'widgy_demo_user',
    }
}

FORCE_SCRIPT_NAME = ''
