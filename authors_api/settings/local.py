from .base import *
from .base import env

DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('DJANGO_SECRET_KEY', default='VdEpHf35MwdGpq4k5Dg-3!#nz!myqi0)i!^r$!dvavi_ve65f!d@9cacg)h_!=30tt5wsi')

ALLOWED_HOSTS = ['localhost', '0.0.0.0', '127.0.0.1']
