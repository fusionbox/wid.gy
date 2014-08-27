from marketing.settings import *

ALLOWED_HOSTS = ['wid.gy', 'www.wid.gy']

DEBUG = False


TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', TEMPLATE_LOADERS),
)


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'KEY_PREFIX': 'widgy_marketing',
    }
}

SENTRY_DSN = 'https://16443522c9664b9d985a32633bc190f0:1f4bcdd5a08b412c846e3a2d9f01bdd3@sentry.fusionbox.com/44'
