# coding=utf-8

from flask import g, request, redirect
from lakers import app
from lakers.services.user import user_core_service

__author__ = 'bug'

class UserMiddleWare(object):
    @staticmethod
    def main():
        session = g.session
        session_data = session.get_session()
        uid_key = app.config.get("SESSION_USER_ID_KEY")
        session_uid = session_data.get(uid_key)
        cookie_uid = request.cookies.get(uid_key)
        if session_uid is None or cookie_uid is None or int(session_uid) != int(cookie_uid):
            session.flush()
            request.user = None
        else:
            user = user_core_service.get_by_id(session_uid)
            request.user = user


