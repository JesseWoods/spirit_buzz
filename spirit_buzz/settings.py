"""
Django settings for spirit_buzz project.
For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SETTINGS_DIR = os.path.dirname(__file__)
PROJECT_PATH = os.path.join(SETTINGS_DIR, os.pardir)
PROJECT_PATH = os.path.abspath(PROJECT_PATH)
TEMPLATE_PATH = os.path.join(PROJECT_PATH, 'templates')
DATABASE_PATH = os.path.join('JesseWoods.mysql.pythonanywhere-services.com')
#DATABASE_PATH = os.path.join('mysql.server')
#JesseWoods.mysql.pythonanywhere-services.com

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'e=7aa5#)1px9crtwn=a5v6egp8ha(3)v+#w^#)4f19k6#7*ml4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ENABLE_SSL = False

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'spiritbuzz',
    #'spiritbuzz.apps.SpiritbuzzConfig',
    'utils',
    'cart',
    #'authorizenet',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'SSLMiddleware.SSLRedirect',
)

#TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
#    TEMPLATE_PATH,
#)


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            TEMPLATE_PATH,
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'utils.context_processors.spiritbuzz',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

ROOT_URLCONF = 'spirit_buzz.urls'

WSGI_APPLICATION = 'spirit_buzz.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'JesseWoods$spiritbuzz',
        'USER': 'JesseWoods',
        'PASSWORD': 'midnite1',
        'HOST': 'JesseWoods.mysql.pythonanywhere-services.com',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_PATH = os.path.join(PROJECT_PATH,'static')
STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')

SITE_NAME = 'SpiritBuzz'
META_KEYWORDS = 'spirits, whiskey, gin, cocktails, liquor'
META_DESCRIPTION = 'SpiritBuzz is an online supplier of small production and local spirits, and innovative cocktail ideas.'

SESSION_ENGINE =  "django.contrib.sessions.backends.signed_cookies"

AUTHNET_POST_URL = 'test.authorize.net'

AUTHNET_POST_PATH = '/gateway/transact.dll'

AUTHNET_DEBUG = True

AUTHNET_LOGIN_ID = "6c7P4qNfju"

AUTHNET_TRANSACTION_KEY = "4C7p2nN63tT3aX43"