from lakers import app
from flask import g, request, redirect
import functools

__author__ = 'bug'

def need_login(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        session = g.session
        session_data = session.get_session()
        uid_key = app.config.get("SESSION_USER_ID_KEY")
        session_uid = session_data.get(uid_key)
        cookie_uid = request.cookies.get(uid_key)
        if session_uid is None or cookie_uid is None or int(session_uid) != int(cookie_uid):
            return redirect('/login/')
        return func(*args, **kw)
    return wrapper
