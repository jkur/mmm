class Config(object):
    SECRET_KEY = 'e9238402842094820394'
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/mmmtest.db'
    # SQLALCHEMY_COMMIT_ON_TEARDOWN=True  ## commit on app_context tearDown
    
class Testing(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class Development(Config):
    TESTING = False
    DEBUG = True
    WTF_CSRF_ENABLED = True


class Development(Config):
    TESTING = False
    DEBUG = False
    WTF_CSRF_ENABLED = True

    # mysql://username:password@server/db
    SQLALCHEMY_DATABASE_URI = 'mysql://mailadmin:password@localhost/mailserver'
    # SQLALCHEMY_ECHO
    # SQLALCHEMY_RECORD_QUERIES
