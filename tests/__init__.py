from flask.ext.testing import TestCase
from nose.tools import raises
from mmm import create_app as app_factory
from mmm import db
from mmm.config import Testing

class MMMTestCase(TestCase):
    def create_app(self):
        return app_factory(__name__, '/', settings_override=Testing())

    def setUp(self):
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        pass

    def test_app_creation(self):
        self.assertIsNotNone(self.app)
