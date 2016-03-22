# -*- coding=utf-8 -*-

from flask.views import MethodView
from flask import render_template

from lakers.common.middleware.before.login_check import need_login


class HandSomeView(MethodView):
    @need_login
    def get(self):
        return render_template("handsome/handsome.html")


class PostHtmlView(MethodView):
    @need_login
    def get(self):
        return render_template("post.html")