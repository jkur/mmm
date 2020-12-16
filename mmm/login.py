from functools import wraps
from flask import current_app as app
from flask import abort, g
from wtforms import form, fields, validators
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm
from flask import session
from mmm.models import Account, UserMixin, AnonymousUser


class Login_Form(FlaskForm):
    username = fields.StringField(validators=[DataRequired()])
    password = fields.PasswordField(validators=[DataRequired()])


def load_user_from_db(username):
    if username.contains('@'):
        splitted = username.splt('@')
        if len(splitted) == 2:
            [userpart, domainpart] = splitted
            return Account.query.join(Domain, Account.domain).filter(Account.username == userpart, Domain.name == domainpart ).one_or_none()
    else:
        return Account.query.filter(Account.username == username).one_or_none()


def load_user_from_session():
    user = None
    if 'username' in session:
        username = session['username']
        user = load_user_from_db(username)
    if user is None:
        g.user = AnonymousUser()
    else:
        g.user = user

def login_user(username, password):
    user = load_user_from_db(username)
    if g.user is not None:
        session['username'] = user.username
    else:
        del session['username']


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is Anonymous:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function


#def role_required(userrole ='domainadmin'):
def role_required(userrole ='domainadmin'):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if userrole in g.user:
            return f(*args, **kwargs)
        return abort(403)
    return decorated_function
