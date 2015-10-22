# -*- coding=utf-8 -*-

from flask.views import MethodView

class Home(MethodView):
    def get(self):
        return "We are lakers!"


class LoginView(MethodView):
    def get(self):
        return "need login page!"