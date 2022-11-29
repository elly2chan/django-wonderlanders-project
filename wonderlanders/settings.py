import os
from pathlib import Path

import cloudinary
from dotenv import dotenv_values
from django.urls import reverse_lazy

config = dotenv_values('envs/.env')

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config['SECRET_KEY']

DEBUG = bool(config['DEBUG'])

ALLOWED_HOSTS = config['ALLOWED_HOSTS'].split(' ')

CSRF_TRUSTED_ORIGINS = [f'https://{x}' for x in ALLOWED_HOSTS]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cloudinary',
    'cart',

    'wonderlanders.common',
    'wonderlanders.posts',
    'wonderlanders.profiles',
    'wonderlanders.products',
    'wonderlanders.store',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'wonderlanders.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processor.cart_total_amount',
                'wonderlanders.common.context_processors.cart_details',
            ],
        },
    },
]

WSGI_APPLICATION = 'wonderlanders.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': config['DB_ENGINE'],
        'NAME': config['DB_NAME'],
        'USER': config['DB_USER'],
        'PASSWORD': config['DB_PASSWORD'],
        'HOST': config['DB_HOST'],
        'PORT': config['DB_PORT'],
    },
}

CACHES = {
    'default': {
        'BACKEND': config['CACHE_BACKEND'],
        'LOCATION': config['CACHE_LOCATION'],
    },
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

STATICFILES_DIRS = [BASE_DIR / 'staticfiles']

MEDIA_URL = 'media/'

# MEDIA_ROOT = BASE_DIR / 'mediafiles'

cloudinary.config(
    cloud_name=config['CLOUD_NAME'],
    api_key=config['API_KEY'],
    api_secret=config['API_SECRET'],
    secure=bool(config['SECURE']),
)

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'profiles.AppUser'

LOGIN_REDIRECT_URL = 'index'

CART_SESSION_ID = 'cart'
