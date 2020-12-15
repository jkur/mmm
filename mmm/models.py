from . import db
import datetime
from sqlalchemy_utils import Timestamp
from flask_login import UserMixin


class User(db.Model, UserMixin, Timestamp):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Unicode(128), index=True)
    password = db.Column(db.Unicode(256))
    #roles = db.relationship('Role', secondary='user_roles')

# Define the Role data-model
#class Role(db.Model):
#    __tablename__ = 'roles'
#    id = db.Column(db.Integer(), primary_key=True)
#    name = db.Column(db.String(50), unique=True)

# Define the UserRoles association table
#class UserRoles(db.Model):
#    __tablename__ = 'user_roles'
#    id = db.Column(db.Integer(), primary_key=True)
#    user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'))
#    role_id = db.Column(db.Integer(), db.ForeignKey('roles.id', ondelete='CASCADE'))



class Domain(db.Model, Timestamp):
    __tablename__ = 'domains'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(250), unique=True, index=True)
    description = db.Column(db.Unicode())


class Account(db.Model, Timestamp):
    __tablename__ = 'accounts'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Unicode(128), index=True)
    domain_id = db.Column(db.Integer, db.ForeignKey('domains.id'), index=True)
    domain = db.relationship('Domain', single_parent=True, backref=db.backref('accounts', lazy='dynamic'))
    password = db.Column(db.Unicode(256))
    active = db.Column(db.Boolean(), default=False)


class Alias(db.Model, Timestamp):
    __tablename__ = 'aliases'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Unicode(128), index=True)
    domain_id = db.Column(db.Integer, db.ForeignKey('domains.id'), index=True)
    domain = db.relationship('Domain', single_parent=True, backref=db.backref('aliases', lazy='dynamic'))
    target = db.Column(db.Unicode(254))
