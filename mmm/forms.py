from flask_wtf import Form
from wtforms import validators
from wtforms import StringField, PasswordField, BooleanField
from mmm.validators import validate_active_user, validate_domain_name, validate_email_username, validate_combined_email_address
from mmm.models import Domain
from mmm.fields import DomainField


class Domain_Form(Form):
    name = StringField('domainname', [validators.Required(message="domainname missing"), validate_domain_name])
    description = StringField()


class Account_Form(Form):
    username = StringField('username', [validators.Required(message="username missing"),
                                        #validate_email_username,
                                        #validate_combined_email_address
                                    ])
    domain = DomainField('domain', [validators.Required(message="select domain")])
    password = PasswordField('password', [validators.Required(message="password missing")])
    active = BooleanField()


class Alias_Form(Form):
    username = StringField('username', [validators.Required(message="username missing"),
                                        validate_email_username,
                                        validate_combined_email_address])
    domain = DomainField('domain', [validators.Required(message="select domain")])
    target = StringField()
