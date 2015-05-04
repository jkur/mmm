from tests import MMMTestCase

from mmm.forms import Domain_Form, Address_Form, Alias_Form, Login_Form
from wtforms import StringField, PasswordField
from wtforms.validators import ValidationError, StopValidation
from datetime import datetime
from mmm.models import Admin
from mmm import db


from mmm.validators import validate_domain_name


class Test_Forms(MMMTestCase):

    def setUp(self):
        with self.app.app_context():
            db.create_all()
        a = Admin(username='admin', password='hallo', active=True)
        a.save(db)

    def tearDown(self):
        pass
    
    def test_login_form(self):
        lf = Login_Form()
        self.assertIsInstance(lf.username, StringField)
        self.assertIsInstance(lf.password, PasswordField)

    def test_login_form_filling(self):
        lf = Login_Form(username="unknown", password="hallo")
        self.assertEqual(lf.username.data, 'unknown')
        self.assertEqual(lf.password.data, 'hallo')


    def test_login_validation(self):
        lf = Login_Form(username="", password="hallo")

        self.assertRaises(ValidationError, lf.validate_on_submit)
        #    lf.validate()
        #e = cm.exception
        #self.assertEqual(str(e), 'Invalid login')

        lf = Login_Form(username="admin", password="halloverkehrt")
        with self.assertRaises(ValidationError) as context:
            lf.validate()
        e = context.exception
        self.assertEqual(e.msg, 'Invalid login')

        lf = Login_Form(username="admin", password="hallo")
        lf.validate()

    #def test_domain_validation(self):
    #    df = Domain_Form(description="Hallo ich bin eine falsche Domain")
    #    self.assertRaises(ValidationError, df.validate)


    def test_validator_domain(self):
        df = Domain_Form(name="www.corsario_o%$rg.nixda", description="Hallo ich bin eine falsche Domain")
        self.assertRaises(ValidationError, validate_domain_name, df, df.name)
        
