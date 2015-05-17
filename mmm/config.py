class Config(object):
    SECRET_KEY = 'e9238402842094820394'
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/mmmtest.db'

class Testing(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class Development(Config):
    TESTING = True
    DEBUG = True
    WTF_CSRF_ENABLED = False
