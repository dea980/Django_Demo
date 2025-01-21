"""
Django settings for SimpleApp project.

This is the main settings file for the SimpleApp project. It contains all the configuration
settings including database configuration, installed apps, middleware setup, and authentication
settings including OAuth configuration.

Key Settings:
- Database: SQLite (development)
- Authentication: Django-allauth with Google OAuth support
- Email: Console backend (development)
- Static files: Default Django configuration
- Time zone: Asia/Seoul

For more information on Django settings, see:
https://docs.djangoproject.com/en/5.1/topics/settings/
"""

from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-&(g5^l2a%yki^42zgas=^^44)pkhvt6yw17t!puc0o^t2c22$6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'accounts',
    'Message_Chat_app',
    'scheduler',
    'debug_toolbar',
]

MIDDLEWARE = [
    ## SecuritySettingsManager
    'django.middleware.security.SecurityMiddleware',
    ## DebugToolbar
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    ## SessionMiddleware
    'django.contrib.sessions.middleware.SessionMiddleware',
    ## CommandManager
    'django.middleware.common.CommonMiddleware',
    ## csrfMiddleware
    'django.middleware.csrf.CsrfViewMiddleware',
    ## AuthenticationMiddleware (after csrfMiddleware)
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    ## MessageMiddleware (after AuthenticationMiddleware)
    'django.contrib.messages.middleware.MessageMiddleware',
    ## X-Frame-OptionsMiddleware
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ## SocialAccountMiddleware (after X-Frame-OptionsMiddleware)
    'allauth.account.middleware.AccountMiddleware',
    ## Signe up시에만 Access 할수 있도록 미들웨어 설정
    'accounts.middleware.SignupRequiredMiddleware',
]

ROOT_URLCONF = 'SimpleApp.urls'

TEMPLATES = [
    {
        ## Template
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        ## directories
        'DIRS': [BASE_DIR / 'templates'],
        ## App direcotories
        'APP_DIRS': True,
        ## Extra context processors
        'OPTIONS': {
            'context_processors': [
                ## Context processors debugging
                'django.template.context_processors.debug',
                ## Context processors request
                'django.template.context_processors.request',
                ## Context processors authorization
                'django.contrib.auth.context_processors.auth',
                ## Context processors messages
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
## WSGI middleware
WSGI_APPLICATION = 'SimpleApp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        ## 엔진 : sqlite3
        'ENGINE': 'django.db.backends.sqlite3',
        ## base path of the database
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

## Authentication Validation
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

## Interal IP 가 필요 ....  testing  IP settings
INTERNAL_IPS = [
    '127.0.0.1',
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Email settings for development
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Django-allauth settings
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

SITE_ID = 1

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

# Additional allauth settings
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
ACCOUNT_EMAIL_VERIFICATION = 'optional'
ACCOUNT_RATE_LIMITS = {
    'login_failed': None  # No limit on failed login attempts
}
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
ACCOUNT_LOGIN_ON_PASSWORD_RESET = True
ACCOUNT_SESSION_REMEMBER = True

# Redirect settings
LOGIN_URL = '/accounts/signup/'  # Default URL for login_required decorator
LOGIN_REDIRECT_URL = '/'  # Where to redirect after successful login/signup
ACCOUNT_SIGNUP_REDIRECT_URL = '/'  # Where to redirect after signup
ACCOUNT_LOGOUT_REDIRECT_URL = '/accounts/signup/'  # Where to redirect after logout
ACCOUNT_LOGIN_ON_PASSWORD_RESET = True
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True

# OpenAI settings
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
