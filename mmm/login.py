from flask import current_app as app
from flask_login import UserMixin
from mmm import login_manager
from wtforms import form, fields, validators
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from mmm.models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class Login_Form(FlaskForm):
    username = fields.StringField(validators=[DataRequired()])
    password = fields.PasswordField(validators=[DataRequired()])
