from wtforms.validators import ValidationError, StopValidation

from mmm.models import Admin, Address, Domain
import re

DOMAIN_REGEX = re.compile(r'^([a-z0-9][a-z0-9-]{1,63}\.){1,6}(org|com|mobi|net|[a-z]{2})$', re.IGNORECASE)

EMAIL_USERNAME_REGEX = re.compile(r"^[A-Z0-9._%+-]+$", re.IGNORECASE)
EMAIL_ADDRESS_REGEX = re.compile(r"^[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}$", re.IGNORECASE)


def validate_login_user(form, field):
    print("field.data", field.data)
    if not Admin.query.filter_by(username=field.data).first():
        print("failed query", field.data)
        raise ValidationError("Invalid login")
    u = Admin.query.filter_by(username=form.data['username']).first()
    if not check_user_password(u, form.data['password']):
        raise ValidationError("Invalid login")
    return True


def validate_active_user(form, field):
    if not Admin.query.filter_by(username=field.data, active=True).first():
        raise ValidationError("Account is not active")


def validate_domain_doesnt_exist(form, field):
    if Domain.query.filter_by(name=field.data).first():
        raise ValidationError("Domain already exists")


def validate_domain_name(form, field):
    if not DOMAIN_REGEX.match(field.data):
        raise ValidationError("Invalid domain name format")


def validate_email_username(form, field):
    if not EMAIL_USERNAME_REGEX.match(field.data):
        raise ValidationError("Invalid username format")


def validate_combined_email_address(form, field):
    if not EMAIL_ADDRESS_REGEX.match("%s@%s" % (form.data['username'], form.data['domain'])):
        raise ValidationError("Invalid email address format")


def validate_email_address(form, field):
    if not EMAIL_ADDRESS_REGEX.match(field.data):
        raise ValidationError("Invalid email address format")


def validate_combined_email_address_doesnt_exist(form, field):
    if Address.query.filter_by(username=form.data['username'],
                               domain=Domain.query.filter_by(name=form.data['domain']).first()
                               ).first():
        raise ValidationError("Account already exists")


def validate_admin_doesnt_exist(form, field):
    if Admin.query.filter_by(username=field.data).first():
        raise ValidationError("Account already exists")
