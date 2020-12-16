from . import db
import datetime
from sqlalchemy_utils import Timestamp
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.ext.declarative import declarative_base



## helpers
class UserMixin():
    def is_admin(self):
        return 'admin' in self.roles

    @property
    def is_authenticated(self):
        return True

class AnonymousUser(UserMixin):
    username = 'anonymous'

    @property
    def is_authenticated(self):
        return False

    roles = ['nobody']


# Define the Role data-model
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)

# Define the UserRoles association table
class AccountRoles(db.Model):
    __tablename__ = 'account_roles'
    id = db.Column(db.Integer(), primary_key=True)
    account_id = db.Column(db.Integer(), db.ForeignKey('accounts.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey('roles.id', ondelete='CASCADE'))


class Domain(db.Model, Timestamp):
    __tablename__ = 'domains'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode(250), unique=True, index=True)
    description = db.Column(db.Unicode())


class Account(db.Model, Timestamp, UserMixin):
    __tablename__ = 'accounts'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Unicode(128), index=True)
    domain_id = db.Column(db.Integer, db.ForeignKey('domains.id'), index=True)
    domain = db.relationship('Domain', single_parent=True, backref=db.backref('accounts'))
    password = db.Column(db.Unicode(256))
    active = db.Column('is_active', db.Boolean(), nullable=False, server_default='1')
    roles = db.relationship('Role', secondary='account_roles')

    @hybrid_property
    def email(self):
        return "{}@{}".format(self.username, self.domain.name)


class Alias(db.Model, Timestamp):
    __tablename__ = 'aliases'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Unicode(128), index=True)
    domain_id = db.Column(db.Integer, db.ForeignKey('domains.id'), index=True)
    domain = db.relationship('Domain', single_parent=True, backref=db.backref('aliases', lazy='dynamic'))
    target = db.Column(db.Unicode(254))
