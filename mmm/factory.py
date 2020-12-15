from flask import Flask
from mmm import db, csrf, mail, migrate, login_manager
from mmm.adminapp import register_admin
from flask_login import LoginManager
import datetime
from mmm.login import load_user
from mmm.login import load_user
from mmm.models import User

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
    login_manager.init_app(app)

    with app.app_context():
        if not User.query.filter(User.username == 'admin').first():
            user = User(
                username = 'admin',
                password='hallo15'
            )
            db.session.add(user)
            db.session.commit()
            print("Added ADmin User!")

    register_admin(app, db)


    from .views import mod
    app.register_blueprint(mod)
    if app.debug:
         app.logger.debug(app.url_map)
    return app
