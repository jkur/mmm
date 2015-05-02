#!/usr/bin/env python
# -*- coding: utf-8 -*-

from werkzeug.serving import run_simple
from mmm import db
from mmm import create_app

application = create_app(settings_override="app.config.Development")

if __name__ == "__main__":
    with application.app_context():
        db.create_all()
    run_simple('0.0.0.0', 5000, application, use_reloader=True, use_debugger=True)
