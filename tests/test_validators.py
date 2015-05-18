from tests import MMMTestCase

from mmm.forms import Domain_Form, Address_Form, Alias_Form, Login_Form
from wtforms import StringField, PasswordField
from wtforms.validators import ValidationError, StopValidation
from datetime import datetime
from mmm.models import Admin, Domain
from mmm import db

from werkzeug import ImmutableMultiDict

from mmm.validators import validate_domain_name, validate_login_user, validate_active_user, validate_combined_email_address, validate_combined_email_address_doesnt_exist


class Test_Validators(MMMTestCase):

    def setUp(self):
        with self.app.app_context():
            db.create_all()
        self.admin_user = Admin(username='admin', password='hallo', active=True)
        self.admin_user.save(db)
        self.inactive_admin_user = Admin(username='admininactive', password='hallo2', active=False)
        self.inactive_admin_user.save(db)

    def tearDown(self):
        pass
    
    def test_login_validation(self):
        with self.app.app_context() as ctx:
            lf = Login_Form(username="df", password="hallo")

            with self.assertRaises(ValidationError) as cm:
                validate_login_user(lf, lf.username)
            e = cm.exception
            self.assertEqual(str(e), 'Invalid login')

            lf = Login_Form(username="admin", password="halloverkehrt")
            with self.assertRaises(ValidationError) as cm:
                validate_login_user(lf, lf.username)
            e = cm.exception
            self.assertEqual(str(e), 'Invalid login')

            lf = Login_Form(username="admin", password="hallo")
            self.assertTrue(validate_login_user(lf, lf.username))


    def test_validator_domain(self):
        df = Domain_Form(name="www.corsario_o%$rg.nixda", description="Hallo ich bin eine falsche Domain")
        self.assertRaises(ValidationError, validate_domain_name, df, df.name)
        
        df = Domain_Form(name="www.corsario.org", description="Hallo ich bin eine richtige Domain")
        self.assertTrue(validate_domain_name(df, df.name))

    def test_validator_active_user(self):
        lf = Login_Form(username="adminnotexists", password="badpassword")
        with self.assertRaises(ValidationError) as ctx:
            validate_active_user(lf, lf.username)
        e = ctx.exception
        self.assertEqual(str(e), "Account is not active")

        # change to inactive user
        lf = Login_Form(username="admininactive", password="hallo")
        with self.assertRaises(ValidationError) as ctx:
            validate_active_user(lf, lf.username)
        e = ctx.exception
        self.assertEqual(str(e), "Account is not active")

        
        df = Domain_Form(name="www.corsario_o%$rg.nixda", description="Hallo ich bin eine falsche Domain")
        self.assertRaises(ValidationError, validate_domain_name, df, df.name)


    def test_validator_email_username(self):
        # True
        d = Domain(name="corsario.org", description="Test")
        d.save(db)
        af = Address_Form(username='jkur', domain=d.id)
        self.assertTrue(validate_combined_email_address(af, af.username))

        # fails: bad username
        af = Address_Form(username='jkur@fjldfd', domain=d.id)
        with self.assertRaises(ValidationError) as ctx:
            validate_combined_email_address(af, af.username)
        e = ctx.exception
        self.assertEqual(str(e), "Invalid email address format")

        # fails: "+" cannot be used as name, because postfix uses it
        af = Address_Form(username='jkur+fdfk', domain=d.id)
        with self.assertRaises(ValidationError) as ctx:
            validate_combined_email_address(af, af.username)
        e = ctx.exception
        self.assertEqual(str(e), "Invalid email address format")

        
    def test_validator_email_username(self):
        d = Domain(name="corsario.org", description="Test")
        d.save(db)
        af = Address_Form(ImmutableMultiDict([('domain', str(d.id)), ('username', 'jkur'), ('active', 'y')]))
        self.assertTrue(validate_combined_email_address(af, af.username))
