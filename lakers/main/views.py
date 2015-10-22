#coding=utf-8

from flask.views import MethodView


class HandSomeAPI(MethodView):
    def get(self):
        return 'handsome get'

    def post(self):
        return 'handsome post'

class Home(MethodView):
    def get(self):
        return "We are lakers!"

