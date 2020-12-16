try:
    from mmm.secrets import mysql_pass
except:
    # define secrets here
    mysql_pass = 'notthepassword'


class Config(object):
    SECRET_KEY = 'e9238402842094820394'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///qmmmtest.db'
    # SQLALCHEMY_COMMIT_ON_TEARDOWN=True  ## commit on app_context tearDown
   # Flask-Mail SMTP server settings
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USE_TLS = False
    MAIL_USERNAME = 'email@example.com'
    MAIL_PASSWORD = 'password'
    MAIL_DEFAULT_SENDER = '"MyApp" <noreply@example.com>'

    # Flask-User settings
    USER_APP_NAME = "Mega Mail Manager"      # Shown in and email templates and page footers
    USER_ENABLE_EMAIL = True        # Enable email authentication
    USER_ENABLE_USERNAME = False    # Disable username authentication
    USER_EMAIL_SENDER_NAME = USER_APP_NAME
    USER_EMAIL_SENDER_EMAIL = "admin@postly.de"


class Testing(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'


class Development(Config):
    TESTING = False
    DEBUG = True
    WTF_CSRF_ENABLED = True


class Production(Config):
    TESTING = False
    DEBUG = False
    WTF_CSRF_ENABLED = True

    # mysql://username:password@server/db
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://mailadmin:%s@localhost/postly' % (mysql_pass)
    # SQLALCHEMY_ECHO
    # SQLALCHEMY_RECORD_QUERIES
