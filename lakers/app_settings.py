import os

from lakers.develop import *

import pytz

ROOT = os.path.dirname(os.path.realpath(__file__))

BEFORE_REQUEST_CLASSES = (
    "common.middleware.before.session.SessionMiddleWare",
    "common.middleware.before.user.UserMiddleWare",
)

AFTER_REQUEST_CLASSED = ''

DEBUG = os.path.exists(os.path.join(ROOT, 'develop.py'))

TIME_ZONE = 'Asia/Shanghai'
APP_TIMEZONE = pytz.timezone(TIME_ZONE)
