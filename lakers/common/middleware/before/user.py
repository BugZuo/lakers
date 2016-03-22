# coding=utf-8

from flask import g, request, redirect
import re
from lakers import app
from lakers.services.user import user_core_service

__author__ = 'bug'

SPIDER_RE = re.compile(r".*Baiduspider|Googlebot|Sogou web spider.*")

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


class RedirectMiddleWare(object):
    """
    根据user_agent判定爬虫请求，过滤
    """
    @staticmethod
    def main():
        need_redirect_path = (
            r'lakers.views.webs.handsome.views.HandSomeView.get./handsome/',
        )
        view_path = request.endpoint
        user_agent = request.user_agent.string
        is_matched = re.match(SPIDER_RE, user_agent)
        print(is_matched.string)
        if view_path in need_redirect_path and not is_matched:
            return redirect('/post/')
