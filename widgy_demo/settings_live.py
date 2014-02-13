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

SENTRY_DSN = 'https://16443522c9664b9d985a32633bc190f0:1f4bcdd5a08b412c846e3a2d9f01bdd3@sentry.fusionbox.com/44'
