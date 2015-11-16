# -*- coding=utf-8 -*-

from flask.views import MethodView

class HandSomeAPI(MethodView):
    def get(self):
        return "HandSomeAPI get"
