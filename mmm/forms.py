
from flask.ext.wtf import Form
from wtforms import validators
from wtforms import StringField, PasswordField, SelectField, BooleanField
from mmm.validators import validate_active_user, validate_login_user, validate_domain_name


class Login_Form(Form):
    username = StringField('Username', [validate_login_user])
                                        #validators.Required(message="Please enter your username"),
                                        #validate_active_user])
                                        
    password = PasswordField('Password', [validate_login_user])
                             #[validators.Required(message="Please enter your password"),
                             #             validate_login_user,
                             #             validate_active_user])


class Domain_Form(Form):
    name = StringField('domainname', [validators.Required(message="domainname missing"), validate_domain_name])
    description = StringField()


class Address_Form(Form):
    username = StringField()
    domain = SelectField()
    password = PasswordField()
    active = BooleanField()

    
class Alias_Form(Form):
    username = StringField()
    domain = SelectField()
    target = StringField()
