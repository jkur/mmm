from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_session import Session
from flask_migrate import Migrate
from flask_mail import Mail
from flask_wtf.csrf import CSRFProtect


db = SQLAlchemy()
session = Session()
migrate = Migrate()
mail = Mail()
csrf = CSRFProtect()
login_manager = LoginManager()
