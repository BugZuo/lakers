# coding=utf-8

import redis

from lakers import app

host = app.config.get('SESSION_REDIS_HOST', 'localhost')
port = app.config.get('SESSION_REDIS_PORT', 6379)
db_number = app.config.get('SESSION_REDIS_DB', 0)
password = app.config.get('SESSION_REDIS_PASSWORD', None)
socket_timeout = app.config.get('SESSION_REDIS_SOCKET_TIMEOUT', 2)

session_server = redis.StrictRedis(
        host=host,
        port=port,
        db=db_number,
        password=password,
        socket_timeout=socket_timeout
    )