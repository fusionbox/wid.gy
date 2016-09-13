from marketing.settings import *

ALLOWED_HOSTS = ['wid.gy', 'www.wid.gy']

DEBUG = False

DATABASES = {'default': dj_database_url.config()}
DATABASES['default']['ATOMIC_REQUESTS'] = True

TEMPLATES[0]['OPTIONS']['loaders'] = (
    ('django.template.loaders.cached.Loader', TEMPLATES[0]['OPTIONS']['loaders']),
)


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'KEY_PREFIX': 'widgy_marketing',
    }
}

SENTRY_DSN = 'https://16443522c9664b9d985a32633bc190f0:1f4bcdd5a08b412c846e3a2d9f01bdd3@sentry.fusionbox.com/44'

MEDIA_ROOT = os.environ['MEDIA_ROOT']
STATIC_ROOT = os.environ['STATIC_ROOT']
