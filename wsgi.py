#!/usr/bin/env python
# -*- coding: utf-8 -*-

from werkzeug.serving import run_simple
from werkzeug import url_decode

from mmm import db
from mmm import create_app


class MethodRewriteMiddleware(object):

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        if 'METHOD_OVERRIDE' in environ.get('QUERY_STRING', ''):
            args = url_decode(environ['QUERY_STRING'])
            method = args.get('__METHOD_OVERRIDE__')
            if method:
                method = method.encode('ascii', 'replace')
                environ['REQUEST_METHOD'] = method
        return self.app(environ, start_response)



application = create_app(__name__, '/', settings_override="mmm.config.Development")

application.wsgi_app = MethodRewriteMiddleware(application.wsgi_app)
if __name__ == "__main__":
    with application.app_context():
        db.create_all()
    run_simple('0.0.0.0', 5000, application, use_reloader=True, use_debugger=True)
