from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
ALLOWED_HOSTS = ['orlando.pythonanywhere.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'orlando$default',
        'USER': 'orlando',
        'PASSWORD': 'OrlandoCana123$',
        'HOST': 'orlando.mysql.pythonanywhere-services.com', 
        'PORT': '3306',   
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
