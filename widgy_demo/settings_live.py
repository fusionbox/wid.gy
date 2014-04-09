from .settings import *

TEMPLATE_DEBUG = DEBUG = False

ALLOWED_HOSTS = [
    'demo.wid.gy',
    'wid.gy',
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

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        'KEY_PREFIX': 'widgy_demo',
    }
}

TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', TEMPLATE_LOADERS),
)

REQUIRE_BUILD_PROFILE = 'widgy.build.js'
REQUIRE_BASE_URL = 'widgy/js'
STATICFILES_STORAGE = 'require.storage.OptimizedStaticFilesStorage'
