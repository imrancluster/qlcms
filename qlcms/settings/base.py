import os
import re

import environ

env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
PROJECT_ROOT = os.path.normpath(os.path.dirname(__file__))
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

SECRET_KEY = 'ay3x4zt&ov-3z$xdzg*b2p9ey@b7deo_s3tb&54x8xcp1dbzq0'

DEBUG = env('DEBUG')

ALLOWED_HOSTS = []
INTERNAL_IPS = ['127.0.0.1']