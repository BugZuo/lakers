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
        decorators = decorators or ()
        if not isinstance(decorators, tuple):
            decorators = (decorators,)
        if isinstance(methods, str):
            methods = (methods,)

        if endpoint is None:
            _module = View.__module__
            _name = View.__name__
            _methods = '_'.join(methods).lower()
            endpoint = '.'.join([_module, _name, _methods, uri])

        if hasattr(View, 'as_view'):  # a flask.views.View (MethodView)
            view = View.as_view(endpoint)
        elif callable(View):
            view = View
        else:
            raise RuntimeError('Unsupported View!')

        for decorator in decorators:
            view = decorator(view)
        self.app.add_url_rule(uri, endpoint=endpoint, view_func=view, methods=methods)