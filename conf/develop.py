
import os

PUBLIC_HOST = '115.28.235.26'

TEMPLATE_FOLDER = 'templates'

STATIC_FOLDER = 'static'

STATIC_PREFIX = ''

SQLALCHEMY_DATABASE_URI = 'mysql://root:asd@115.28.235.26:3306/lakers'
SQLALCHEMY_POOL_SIZE = 5

MONGO_HOST = PUBLIC_HOST
MONGO_PORT = 27017

SESSION_REDIS_HOST = PUBLIC_HOST
SESSION_REDIS_PORT = 6379
SESSION_REDIS_DB = 0
SESSION_REDIS_PASSWORD = None
SESSION_REDIS_SOCKET_TIMEOUT = 2

SECRET_KEY = 'lakers'
# Age of cookie, in seconds (default: 2 weeks).
SESSION_COOKIE_AGE = 60 * 60 * 24 * 1
# Whether a user's session cookie expires when the Web browser is closed.
SESSION_EXPIRE_AT_BROWSER_CLOSE = False
SESSION_COOKIE_AGE_LOGIN_USER = 60 * 60 * 24 * 14

# Cookie name. This can be whatever you want.
SESSION_COOKIE_NAME = 'session_id'
SESSION_USER_ID_KEY = 'laker_id'