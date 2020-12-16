# coding: utf-8
from mmm.models import Account, Domain
from passlib.hash import md5_crypt, sha256_crypt, sha512_crypt
from passlib.context import CryptContext
from base64 import b64decode, b64encode
from flask import g

pwd_context = CryptContext(
    # Replace this list with the hash(es) you wish to support.
    # this example sets pbkdf2_sha256 as the default,
    # with additional support for reading legacy des_crypt hashes.
    schemes=["bcrypt", "sha512_crypt"],

    # Automatically mark all but first hasher in list as deprecated.
    # (this will be the default in Passlib 2.0)
    deprecated="auto",

    # Optionally, set the number of rounds that should be used.
    # Appropriate values may vary for different schemes,
    # and the amount of time you wish it to take.
    # Leaving this alone is usually safe, and will use passlib's defaults.
    ## pbkdf2_sha256__rounds = 29000,
    )


def login_user_from_db(username, password):
    user = get_user(username)
    if user is None: return False
    if check_user_password(user, password):
        #login_user(user)
        g.user = user
        return True
    return False


def get_user(username):
    try:
        [account_name, domain] = username.split('@')
        user = Account.query.join(Domain, Account.domain).filter(Account.username == account_name, Domain.name == domain).one_or_none()
    except:
        return None
    return user



def check_user_password(user, password):
    if check_local_user_password(user, password):
        return True
    return check_encrypted_user_password(user, password)

def check_local_user_password(user, password):
    return user.password == password

def check_encrypted_user_password(user, password):
    if user.password.startswith("{"):
        return pwd_context.verify(password, user.password[14:])
    else:
        return pwd_context.verify(password, user.password)
