# -*- coding=utf-8 -*-

from flask.views import MethodView

class HandSomeAPI(MethodView):
    def get(self):
        return "HandSomeAPI get"


class HandSomeView(MethodView):
    def get(self):
        return "HandSomeView get"