from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


db = SQLAlchemy()
app = None


def create_app(package_name, package_path, settings_override=None, **kwargs):
    global app
    app = Flask(__name__, **kwargs)
    app.config.from_object('mmm.config.Config')
    app.config.from_pyfile('settings.cfg', silent=True)
    app.config.from_object(settings_override)

    from .views import mod
    app.register_blueprint(mod)
    db.init_app(app)
    print(app.url_map)
    return app
