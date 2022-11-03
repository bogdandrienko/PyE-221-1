"""
Django settings for django_settings project.

Generated by 'django-admin startproject' using Django 4.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-euondgya4^3-rs@$_%sqr4!d_ruyo1io9*$c%wgi)5e-8_7r#l'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
SQLITE = True

ALLOWED_HOSTS = ['*']


# Application definition

# если приложение не подключено, то миграции не будут выполнены!!!
INSTALLED_APPS = [
    'grappelli',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django_app',
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

ROOT_URLCONF = 'django_settings.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_settings.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

if SQLITE:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'database/db.sqlite3',
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'django_db',
            'USER': 'django_usr',
            'PASSWORD': '12345qwertY!',
            'HOST': '127.0.0.1',  # localhost
            'PORT': '5432',
        }
    }
    # DATABASES = {
    #     'default': {
    #         'ENGINE': 'django.db.backends.mysql',
    #         'NAME': 'django_db',
    #         'USER': 'django_usr',
    #         'PASSWORD': '12345qwertY!',
    #         'HOST': '127.0.0.1',  # localhost
    #         'PORT': '3306',
    #     }
    # }


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'Etc/GMT-6'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'  # префикс ссылки на статический файл
if DEBUG:
    STATICFILES_DIRS = [
        Path(BASE_DIR / 'static'),
        Path(BASE_DIR / 'static_external'),
        Path(BASE_DIR / 'frontend/build/static'),
        Path(BASE_DIR / 'frontend/public/static'),
    ]
else:
    STATIC_ROOT = Path(BASE_DIR / 'static')  # путь на статические файлы (на линуксе статику будет отдавать nginx)
    STATICFILES_DIRS = [
        Path(BASE_DIR / 'static_external'),
        Path(BASE_DIR / 'frontend/build/static'),
        Path(BASE_DIR / 'frontend/public/static'),
    ]

# файлы, загружаемые пользователями (аватарки...)
MEDIA_URL = 'media/'
MEDIA_ROOT = Path(BASE_DIR, 'static/media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
