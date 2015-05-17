from tests import MMMTestCase

from mmm.forms import Domain_Form, Address_Form, Alias_Form, Login_Form
from wtforms.validators import ValidationError
from mmm import db
from mmm.models import Admin, Domain, Address
from flask import url_for

import re

class Test_App(MMMTestCase):

    #def setUp(self):
    #    with self.app.app_context():
    #        db.create_all()
    #    a = Admin(username='admin', password='hallo', active=True)
    #    a.save(db)

    def tearDown(self):
        pass
    
    #def test_login(self):
    #    lf = Login_Form()
    #    self.assertIsInstance(lf.username, StringField)
    #    self.assertIsInstance(lf.password, PasswordField)

    def test_domain_save(self):
        result = self.client.post('/domain', data=dict(name="www.corsario.org", description="test"))
        self.assertRedirects(result, url_for('.domain'))
        d = Domain.query.first()
        self.assertIsNotNone(d)
        self.assertEqual(d.name, "www.corsario.org")
        self.assertEqual(d.description, "test")
        
        
    def test_domain_save_fail(self):
        result = self.client.post('/domain', data=dict(name="www.corsario.org.dddd", description="test"))
        self.assert200(result)
        self.assertEqual(self.get_context_variable('domainform').name.errors[0], "Invalid domain name format")

        result = self.client.post('/domain', data=dict(name="", description="test"))
        self.assert200(result)
        self.assertEqual(self.get_context_variable('domainform').name.errors[0], "domainname missing")

    def test_address_save(self):
        d = Domain(name="corsario.org", description="bluba")
        d = d.save(db)
        result = self.client.post('/address',
                                  data=dict(username="jkur", password="test", domain=d.id),
                                  follow_redirects=True)
        self.assertTrue("jkur@corsario.org" in str(result.data))
        #print(result.data)
        u = Address.query.first()
        self.assertIsNotNone(u)
        self.assertEqual(u.username, "jkur")
        self.assertEqual(u.password, "test")
        self.assertEqual(u.domain.name, "corsario.org")
        
