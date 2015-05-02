from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def create_app(package_name, package_path, settings_override=None, **kwargs):
    app = Flask(__name__, **kwargs)
    app.config.from_object('mmm.config.Config')
    app.config.from_pyfile('settings.cfg', silent=True)
    app.config.from_object(settings_override)

    db.init_app(app)
    return app
