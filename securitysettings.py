import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Runs on localhost only
URL = '127.0.0.1'

# This token is the token the test user is identified with during API-tests
token_test_user = '0'

# Database to your django database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'localhost'
    }
}

PLAYGROUNDS = ('sandbox')

# This is unnecessary as long DEBUG is True
ALLOWED_HOSTS = [] if DEBUG else ['localhost']

# This database connection is used for the actual data interfaces (App: dataedit)
dbuser = "postgres"
dbpasswd = "postgres"
dbport = 5432
dbhost = "localhost"
dbname = "dataedit"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CONTACT_ADDRESSES = {
    'technical': ['tech@localhost'],
    'other': ['other@localhost']
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_USE_TLS = False
EMAIL_PORT = 1025

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

if not DEBUG:
    AUTHENTICATION_BACKENDS = ['login.models.UserBackend']
