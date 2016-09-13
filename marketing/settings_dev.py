from .settings import *

DEBUG = True

ALLOWED_HOSTS = [
    'widgy.dev.fusionbox.com',
]

FORCE_SCRIPT_NAME = ''

SENTRY_DSN = 'https://16443522c9664b9d985a32633bc190f0:1f4bcdd5a08b412c846e3a2d9f01bdd3@sentry.fusionbox.com/44'

MEDIA_ROOT = os.environ['MEDIA_ROOT']
STATIC_ROOT = os.environ['STATIC_ROOT']
