from . import db
import datetime

from sqlalchemy_utils.types.password import PasswordType


class MMM_Model():
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime())
    modified_at = db.Column(db.DateTime())

    def save(self, db):
        self.modified_at = datetime.datetime.now()
        db.session.add(self)
        db.session.commit()
        return self


class Admin(db.Model, MMM_Model):
    __tablename__ = 'admins'

    username = db.Column(db.Unicode(128), unique=True, index=True)
    password = db.Column(db.Unicode(128))
    active = db.Column(db.Boolean())


class Domain(db.Model, MMM_Model):
    __tablename__ = 'domain'

    name = db.Column(db.Unicode(250), unique=True, index=True)
    description = db.Column(db.Unicode())


class Address(db.Model, MMM_Model):
    __tablename__ = 'addresses'

    username = db.Column(db.Unicode(128), index=True)
    domain_id = db.Column(db.Integer, db.ForeignKey('domain.id'), index=True)
    domain = db.relationship('Domain', single_parent=True, backref=db.backref('addresses', lazy='dynamic'))
    password = db.Column(PasswordType(
        schemes=[
            'md5_crypt'
        ],

        #deprecated=['md5_crypt']
    ))
    active = db.Column(db.Boolean(), default=False)



class Alias(db.Model, MMM_Model):
    __tablename__ = 'aliases'

    username = db.Column(db.Unicode(128), index=True)
    domain_id = db.Column(db.Integer, db.ForeignKey('domain.id'), index=True)
    domain = db.relationship('Domain', single_parent=True, backref=db.backref('aliases', lazy='dynamic'))
    target = db.Column(db.Unicode(254))
