from flask import Flask
from mmm import db, csrf, mail, migrate
from mmm.adminapp import register_admin
import datetime
from mmm.models import Account
from mmm.login import load_user_from_session
from flask_simplelogin import SimpleLogin


def create_app(settings_override=None, **kwargs):
    app = Flask(__name__, **kwargs)
    app.config.from_object('mmm.config.Config')
    app.config.from_pyfile('settings.cfg', silent=True)
    app.config.from_object(settings_override)
    app.config.from_envvar('MMM_SETTINGS', silent=True)

    db.init_app(app)
    csrf.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db)
    #SimpleLogin(app, login_checker=only_chuck_norris_can_login)
    SimpleLogin(app)

    from .views import mod as standardmod
    app.register_blueprint(standardmod)

    register_admin(app, db)

    #@app.before_request
    #def load_user():
    #    load_user_from_session()

    if app.debug:
         app.logger.debug(app.url_map)
    return app
