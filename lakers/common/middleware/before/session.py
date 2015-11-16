# coding=utf-8

__author__ = 'bug'

from flask import g, request
from lakers import app
from lakers.ext.session.store import SessionStore

class SessionMiddleWare(object):
    @staticmethod
    def main():
        cookie_name = app.config.get('SESSION_COOKIE_NAME')
        session_id = request.cookies.get(cookie_name)
        session = SessionStore(session_id)
        g.session = session
        request.session = session
