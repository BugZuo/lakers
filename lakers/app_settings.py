import os

from lakers.develop import *

import pytz

ROOT = os.path.dirname(os.path.realpath(__file__))

BEFORE_REQUEST_CLASSES = (
    "common.middleware.before.session.SessionMiddleWare",
    "common.middleware.before.user.UserMiddleWare",
    # "common.middleware.before.user.RedirectMiddleWare",
)

AFTER_REQUEST_CLASSES = (
    "common.middleware.after.cookie.CookieMiddleWare",
)

DEBUG = os.path.exists(os.path.join(ROOT, 'develop.py'))

TIME_ZONE = 'Asia/Shanghai'
APP_TIMEZONE = pytz.timezone(TIME_ZONE)

SESSION_SAVE_EVERY_REQUEST = False
SESSION_COOKIE_DOMAIN = 'www.flyzfq.com'
SESSION_COOKIE_SECURE = False                           # Whether the session cookie should be secure (https:// only).
SESSION_COOKIE_PATH = '/'                               # The path of the session cookie.
SESSION_COOKIE_HTTPONLY = False                         # Whether to use the non-RFC standard httpOnly flag (IE, FF3+, others)
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
