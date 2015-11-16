# coding=utf-8

import importlib

__author__ = 'bug'


class MiddleWare(object):
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        self.register_before_request_funcs()
        self.register_after_request_funcs()

    def register_before_request_funcs(self):
        wares = self.app.config.get('BEFORE_REQUEST_CLASSES', '')
        f = self.app.before_request
        self._register(wares, f)

    def register_after_request_funcs(self):
        wares = self.app.config.get('AFTER_REQUEST_CLASSES', '')
        f = self.app.after_request
        self._register(wares, f)

    def _register(self, wares, f):
        for ware in wares:
            tmps = ware.split('.')
            module_path = self.app.name + '.' + '.'.join(tmps[:-1])
            class_name = tmps[-1]
            module = importlib.import_module(module_path)
            _class = getattr(module, class_name)
            func = _class.main
            f(func)

