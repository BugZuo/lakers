# -*- coding=utf-8 -*-

from flask.views import MethodView
from flask import render_template
from flask import request

class Home(MethodView):
    def get(self):
        return "We are lakers!"


class LoginView(MethodView):
    def get(self):
        return render_template("login/login.jinja")

    def post(self):
        username = request.form.get('username', 'baby')
        password = request.form.get('password', 'baby')
        return "good girl!"