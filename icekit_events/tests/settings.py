"""
Test settings for ``icekit_events`` app.
"""

import os

BASE_DIR = os.path.dirname(__file__)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'test_icekit_events',
        'ATOMIC_REQUESTS': True,
        'TEST': {
            'NAME': 'test_icekit_events',
            # See: https://docs.djangoproject.com/en/1.7/ref/settings/#serialize
            'SERIALIZE': False,
        },
    }
}

DEBUG = True
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SITE_DOMAIN = SITE_NAME = 'localhost'
SITE_PORT = '8080'
SITE_ID = 1

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django_nose',
    'fluent_pages',
    'fluent_contents',

    'icekit_events',
    'icekit_events.event_types.simple',
    'icekit_events.page_types.eventlistingfordate',
    'icekit_events.tests',

    # ICEkit modules must be loaded *after* events to avoid import errors
    'icekit',
    'icekit.workflow',
    'icekit.publishing',
    'icekit.plugins.image',

    # Apps required for publishing features
    'model_settings',
    'polymorphic',
    'compressor',

    # Test ICEKit pages etc
    'django.contrib.sites',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'icekit.publishing.middleware.PublishingMiddleware',
)

ROOT_URLCONF = 'icekit_events.tests.urls'
SECRET_KEY = 'secret-key'
STATIC_URL = '/static/'
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'  # Default: django.test.runner.DiscoverRunner
TIME_ZONE = 'Australia/Sydney'  # Default: America/Chicago
USE_TZ = True  # Default: False
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

DDF_FILL_NULLABLE_FIELDS = False
FLUENT_PAGES_TEMPLATE_DIR = os.path.join(BASE_DIR, '..', 'templates')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'DIRS': [
            os.path.join('icekit_events', 'tests', 'templates'),
            os.path.join('icekit_events', 'templates'),
        ],
        'OPTIONS': {
            'context_processors': [
                'django.core.context_processors.request',
            ],
        },
    },
]
