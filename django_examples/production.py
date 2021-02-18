from .settings import *

import django_heroku
import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = False
ALLOWED_HOSTS = [os.environ['HOST']]

# Activate Django-Heroku.
django_heroku.settings(locals())
try:
    del DATABASES['default']['OPTIONS']['sslmode']  # No SSL required
except:
    pass
