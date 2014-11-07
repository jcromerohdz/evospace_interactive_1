"""
Django settings for evoSpaceInteractive project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""
#FaceBook backends

FACEBOOK_APP_ID = '614898388619931'
FACEBOOK_APP_SECRET = '91e97c60f55b514a3e938d43cae9d585'
FACEBOOK_REDIRECT_URL = 'http://localhost:7070/facebook/login'
AUTHENTICATION_BACKENDS = (
    'shapes.backends.FacebookBackend',
)


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l*m$8)o(y_)fms7nsl!z#@vglx2a3r3v=!ykr_d1fa8*q+1dm)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social.apps.django_app.default',
    'shapes',

)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

# AUTHENTICATION_BACKENDS = (
#     'social.backends.facebook.FacebookOAuth2',
#     'social.backends.facebook.FacebookAppOAuth2',
#     'django.contrib.auth.backends.ModelBackend',
# )

# TEMPLATE_CONTEXT_PROCESSORS = (
#     "django.contrib.auth.context_processors.auth",
#     "django.core.context_processors.debug",
#     "django.core.context_processors.i18n",
#     "django.core.context_processors.media",
#     "django.core.context_processors.static",
#     "django.core.context_processors.tz",
#     "django.contrib.messages.context_processors.messages",
#     'social.apps.django_app.context_processors.backends',
#     'social.apps.django_app.context_processors.login_redirect',
# )

ROOT_URLCONF = 'evoSpaceInteractive.urls'

# WSGI_APPLICATION = 'evoSpaceInteractive.wsgi.application'




# #Fecebook Auth
# SOCIAL_AUTH_FACEBOOK_KEY = '614898388619931'
# SOCIAL_AUTH_FACEBOOK_SECRET = '91e97c60f55b514a3e938d43cae9d585'
# SOCIAL_AUTH_FACEBOOK_SCOPE = ['email', 'user_friends']
# SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {'locale': 'ru_RU'}

# LOGIN_REDIRECT_URL = '/'

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'NAME': 'evospace_i_data',
        'USER': 'chris',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}


# SOCIAL_AUTH_PIPELINE = (
#     'social.pipeline.social_auth.social_details',
#     'social.pipeline.social_auth.social_uid',
#     'social.pipeline.social_auth.auth_allowed',
#     'social.pipeline.social_auth.social_user',
#     'social.pipeline.social_auth.associate_user',
#     'social.pipeline.social_auth.load_extra_data',
#     'social.pipeline.user.user_details',
#     'shapes.pipeline.custom_pipline',
# )
# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

#Template location
TEMPLATE_DIRS = (
    os.path.join(os.path.dirname(BASE_DIR), "static", "templates"),
)

#TEMPLATE_DIRS = [os.path.join(BASE_DIR, 'templates')]
if DEBUG:
    MEDIA_URL='/media/'
    STATIC_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static", "static-only")
    MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), "static", "media")
    STATICFILES_DIRS = (
            os.path.join(os.path.dirname(BASE_DIR), "static", "static"),
        )
