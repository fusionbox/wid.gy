"""
Django settings for widgy_demo project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import imp

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'wy8(9zq6$g1u1nno-$a-1ga=*pykm@x%o$-94bs5syu*fw4c2)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'mezzanine.boot',
    'mezzanine.conf',
    'mezzanine.core',
    'mezzanine.generic',
    'mezzanine.pages',
    'django.contrib.comments',
    'filebrowser_safe',
    'grappelli_safe',

    'widgy',
    'widgy.contrib.page_builder',
    'widgy.contrib.form_builder',
    'widgy.contrib.widgy_mezzanine',
    # 'widgy.contrib.urlconf_include',
    'widgy.contrib.review_queue',

    'django.contrib.admin',

    'filer',
    'easy_thumbnails',
    'compressor',
    'scss',
    'sorl.thumbnail',
    'south',
    'debug_toolbar',
    'django_extensions',
    'argonauts',
    'raven.contrib.django',

    'backupdb',

    'demo.demo_widgets',
    'widgy_demo_app',
    'marketing',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'subdomains.middleware.SubdomainURLRoutingMiddleware',
    'raven.contrib.django.middleware.Sentry404CatchMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'mezzanine.core.request.CurrentRequestMiddleware',
    'mezzanine.core.middleware.AdminLoginInterfaceSelectorMiddleware',
    'mezzanine.pages.middleware.PageMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.static",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "mezzanine.conf.context_processors.settings",
)

ROOT_URLCONF = 'widgy_demo.urls'

SUBDOMAIN_URLCONFS = {
    None: 'marketing.urls',
    'www': 'marketing.urls',
    'demo': 'widgy_demo.urls',
}

WSGI_APPLICATION = 'widgy_demo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = False
USE_L10N = False
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_FINDERS = (
    'compressor.finders.CompressorFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

COMPRESS_ENABLED = True
WIDGY_ROOT = imp.find_module('widgy')[1]
SCSS_IMPORTS = (
    os.path.join(WIDGY_ROOT, 'static', 'widgy', 'css'),
)

# COMPRESS_PRECOMPILERS = (
#     ('text/x-scss', 'django_pyscss.compressor.DjangoScssFilter'),
# )
COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'python -mscss.tool --no-compress'
                    ' --load-path={load_paths}'.format(
                        load_paths=','.join(['"%s"' % d for d in SCSS_IMPORTS]),
                    )),
)

# Mezzanine

PACKAGE_NAME_FILEBROWSER = "filebrowser_safe"
PACKAGE_NAME_GRAPPELLI = "grappelli_safe"
ADMIN_MEDIA_PREFIX = STATIC_URL + "grappelli/"
TESTING = False
GRAPPELLI_INSTALLED = True
SITE_ID = 1

ADD_MENU_ORDER = (
    'widgy_mezzanine.WidgyPage',
)

ADMIN_MENU_ORDER = [
    ('Widgy', (
        'pages.Page',
        'page_builder.Callout',
        'form_builder.Form',
        ('Review queue', 'review_queue.ReviewedVersionCommit'),
        'filer.Folder',
    )),
]

# Widgy

WIDGY_MEZZANINE_SITE = 'widgy_demo.widgy_site.site'


# Copy stuff over from django-widgy/demo
STATICFILES_DIRS = (
    os.path.join(WIDGY_ROOT, '..', 'demo', 'public'),
)

TEMPLATE_DIRS = (
    os.path.join(WIDGY_ROOT, '..', 'demo', 'templates'),
)

# requirejs

# REQUIRE_BUILD_PROFILE = 'widgy.build.js'
# REQUIRE_BASE_URL = 'widgy/js'
# STATICFILES_STORAGE = 'require.storage.OptimizedStaticFilesStorage'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'root': {
        'level': 'WARNING',
        'handlers': ['sentry'],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'sentry': {
            'level': 'INFO',
            'class': 'raven.contrib.django.handlers.SentryHandler',
            'filters': ['require_debug_false'],
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
    },
}

SENTRY_DSN = None
