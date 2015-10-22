# -*- coding=utf-8 -*-

class RESTful(object):
    def __init__(self, app=None):
        self.app = app
        if self.app is not None:
            self.init_app(app)

    def init_app(self, app):
        uris = self.app.config.get('URLS')
        for uri in uris:
            self.register_uri(*uri)  # *uri传入一个list参数，参数依次对应
            # app.add_url_rule(uri[0], methods=uri[1], view_func=uri[2].as_view('%s' % uri[0]))

    def register_uri(self, uri, methods, View, decorators=None, endpoint=None):
        self.app.add_url_rule(uri, methods=methods, view_func=View.as_view('%s' % uri))