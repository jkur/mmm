class Config(object):
    SECRET_KEY = 'e9238402842094820394'


class Testing(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False
