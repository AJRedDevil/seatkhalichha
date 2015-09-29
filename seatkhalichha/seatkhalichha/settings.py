"""
Django settings for thm project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_PATH = os.path.dirname(os.path.abspath(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['LOCAL_SECRET_KEY']

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    # 'django.contrib.admin',
    'south',
    'pipeline',
    'apps.users',
    'apps.search',
    'floppyforms',
    # 'apps.faq',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# AUTH BACKEND DEFINITIONS
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

# TEMPLATE CONTEXT DEFINITIONS
TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    # 'django.contrib.auth.context_processors.auth',
)
# TEMPLATE PATH CONFIGURATION
TEMPLATE_PATH = os.path.join(PROJECT_PATH, 'templates')
TEMPLATE_DIRS = (TEMPLATE_PATH)
## MISCELLANEOUS SETTINGS
ROOT_URLCONF = 'seatkhalichha.urls'
WSGI_APPLICATION = 'seatkhalichha.wsgi.application'
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kathmandu'
USE_I18N = True
USE_L10N = True
USE_TZ = True
APPEND_SLASH = True
# TURN DEBUG OFF
DEBUG = False
TEMPLATE_DEBUG = False
ALLOWED_HOSTS = ['*']

# DATABASE ENGINE CONFIGURATIONS
import dj_database_url
DATABASES = {
    "default": dj_database_url.config()
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

# Static asset configuration
# STATIC_URL = 'http://s3.amazonaws.com/%s/' % AWS_STATIC_BUCKET
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH, 'static'),
)
# Use local storage
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')
MEDIA_URL = '/media/'
# CONFIGURING USERPROFILE AS THE AUTH BACKEND
AUTH_USER_MODEL = 'users.UserProfile'
# LOGIN URL DEFINITIONS
LOGIN_URL = '/signin/'
LOGIN_REDIRECT_URL = '/home/'
URL='https://www.thehomerepairapp.com'
## LOGGING DEFINITION AND CONFIGURATION

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True
        },
        'null': {
            'level': 'WARN',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'WARN',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'mail_admins'],
            'propagate': True,
            'level': 'WARN',
        },
    }
}

# ALL OTHER SETTINGS
# Mandrill API KEY
MANDRILL_API_KEY = os.environ['MANDRILL_API_KEY']
EMAIL_BACKEND = "djrill.mail.backends.djrill.DjrillBackend"
ADMIN_EMAIL = os.environ['ADMIN_EMAIL']
# ERROR REPORTING
DEFAULT_FROM_EMAIL = 'server@seatkhalichha.com'
SERVER_EMAIL = 'server@seatkhalichha.com'
EMAIL_HOST = 'localhost'
EMAIL_PORT = 25
ADMINS = (
    ('Gaurav Ghimire', ADMIN_EMAIL),
)
MANAGERS = ADMINS

#GOOGlE RELATED CONFIGURATIONS
GOOOGLE_API_KEY = os.environ['GOOGLE_API_KEY']

# Phone number setting
PHONENUMBER_DEFAULT_REGION = 'NP'

# LOCAL CONFIG IMPORT, IMPORTS ALL CONFIG FROM local_setting.py,
# required only for a dev env

try:
    from local_setting import *
except ImportError:
    pass


# # for static file management
STATICFILES_STORAGE = 'pipeline.storage.PipelineCachedStorage'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'pipeline.finders.PipelineFinder',
)
PIPELINE_SASS_BINARY = "sassc"
PIPELINE_COMPILERS = (
    'pipeline.compilers.sass.SASSCompiler',
)

PIPELINE_CSS = {
    'web_yellow': {
        'source_filenames': (
          'css/web_yellow.sass',
          'css/popup.css',
        ),
        'output_filename': 'css/web_yellow.css',
    },
    'signin': {
        'source_filenames': (
            'css/animate.css',
            'css/webstyle.css',
        ),
        'output_filename': 'css/signin.css',
    },
    'admin': {
        'source_filenames': (
          'css/bootstrap.css',
          'css/admin.sass',
        ),
        'output_filename': 'css/admin.css',
    },
}
