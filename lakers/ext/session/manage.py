# coding=utf-8

__author__ = 'bug'

from lakers import app
from flask import g, request
from lakers.ext.session.store import SessionStore

DEFAULT_CHARSET = 'utf-8'
SESSION_COOKIE_AGE = app.config.get('SESSION_COOKIE_AGE')

def save_session(user_id, user_name):
    cookie_name = app.config.get('SESSION_COOKIE_NAME')
    uid_key = app.config.get('SESSION_USER_ID_KEY')
    session = g.session
    session.cycle_key()
    session.set_session({
        uid_key: user_id,
        'user_name': user_name,
    })
    session.save()

def store_cookie(response, user_id, user_name=None):
    """
    store cookie in browser
    :param response:
    :param user_id:
    :param user_name:
    :return:
    """
    response.set_cookie(app.config.get('SESSION_USER_ID_KEY'), value=bytes(user_id), max_age=SESSION_COOKIE_AGE)
    # response.set_cookie(app.config.get('SESSION_COOKIE_NAME'), value=bytes(g.session.get_id()), max_age=SESSION_COOKIE_AGE)
    return response

