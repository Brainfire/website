import os
import dj_database_url

# Django settings for brainfire project.
APPS_DIR = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
TOP_DIR = os.path.dirname(APPS_DIR)

DEBUG = os.getenv('DEBUG', False)
TEMPLATE_DEBUG = True

DATABASES = {'default': dj_database_url.config(default='postgres://localhost/brainfire')}

CACHES = {
    'default': {
        'BACKEND': 'django_pylibmc.memcached.PyLibMCCache'
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/Chicago'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(APPS_DIR, 'static/'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
    'compressor.finders.CompressorFinder',
)

if os.getenv('ENABLE_AWS', "False") == "True":
# Setup S3 Static Files
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
    STATICFILES_STORAGE = 'common.storage.CachedS3BotoStorage'
    STATIC_S3_PATH = "static"
    AWS_ACCESS_KEY_ID = os.environ['AWS_KEY']
    AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_KEY']
    AWS_STORAGE_BUCKET_NAME = os.environ['STATIC_BUCKET_NAME']
    AWS_QUERYSTRING_AUTH = False
    COMPRESS_URL = os.getenv('COMPRESS_URL', 'http://{}.s3.amazonaws.com/static/'.format(AWS_STORAGE_BUCKET_NAME))
    STATIC_URL = COMPRESS_URL
    ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'
    COMPRESS_ROOT = STATIC_ROOT
    COMPRESS_ENABLED = os.getenv('COMPRESS_ENABLED', False)
    COMPRESS_STORAGE = STATICFILES_STORAGE
    COMPRESS_OFFLINE = True
    AWS_HEADERS = {
        'Cache-Control': 'public, max-age=31536000', #(1 year)
    }

# Make this unique, and don't share it with anybody.
SECRET_KEY = os.getenv('SECRET_KEY', '8kjr86@v_#-=#+h*fneyf$*_ab1)jpd9#34#i7ew6+w@0er94&amp;')

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'raven.contrib.django.middleware.Sentry404CatchMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'brainfire.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'brainfire.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(APPS_DIR, 'templates/'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    "common.context_processors.common_settings",
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'compressor',
    'common',
    'gunicorn',
    'storages',
    'raven.contrib.django',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

ASSETS = (
    'favicon.ico',
    'robots.txt',
    'humans.txt',
)

SITE_TITLE = 'Brainfire'
SITE_TAGLINE = 'Iginiting Technology'

ENABLE_ZENDESK = os.getenv('ENABLE_ZENDESK', False)

GOOGLE_ANALYTICS_ID = os.getenv('GOOGLE_ANALYTICS_ID', None)
GOOGLE_ANALYTICS_DOMAIN = os.getenv('GOOGLE_ANALYTICS_DOMAIN', None)

RAVEN_CONFIG = {
    'dsn': os.getenv("RAVEN_DSN", None),
}