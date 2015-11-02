# -*- coding=utf-8 -*-

from flask.views import MethodView
from flask import render_template

class HandSomeAPI(MethodView):
    def get(self):
        return "HandSomeAPI get"


class HandSomeView(MethodView):
    def get(self):
        return render_template("handsome/handsome.html")