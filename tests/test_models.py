from tests import MMMTestCase

from mmm.models import Domain, Address, Alias
from mmm import db
from datetime import datetime


class Test_Models(MMMTestCase):
    def test_base_model(self):
        mm = Domain()
        mm.created_at = datetime.now()
        mm_saved = mm.save(db)
        self.assertEqual(mm.id, 1)

    def test_domain_model(self):
        mm = Domain(name='corsario.org')
        mm.created_at = datetime.now()
        mm_saved = mm.save(db)
        self.assertEqual(mm_saved.id, 1)
        self.assertEqual(mm_saved.name, 'corsario.org')

    def test_domain_query(self):
        mm = Domain(name='corsario.org')
        mm.save(db)
        result = Domain.query.get(1)
        self.assertEqual(result.id, 1)
        self.assertEqual(result.name, 'corsario.org')

    def test_address_model(self):
        mm = Address(username='jkur')
        mm.created_at = datetime.now()
        mm_saved = mm.save(db)
        self.assertEqual(mm_saved.id, 1)
        self.assertEqual(mm_saved.username, 'jkur')

    def test_address_model_with_ref_to_domain(self):
        addr = Address(username='jkur')
        domain = Domain(name='corsario.org')
        addr.save(db)
        addr.domain = domain
        addr.save(db)
        addr.created_at = datetime.now()
        addr_saved = addr.save(db)
        addr.password = "hallo"
        h = '$1$B.vGnUpI$h9DyhJ0Us0jT/lg0g4jGK.'
        self.assertEqual(addr_saved.id, 1)
        self.assertEqual(addr_saved.username, 'jkur')
        self.assertEqual(addr_saved.domain.name, 'corsario.org')
        #self.assertEqual(str(addr_saved.password), "hallo")
        #print(addr_saved.password)
        #self.assertTrue(addr_saved.password == "hallo")
        #assert addr_saved.password == b'hallo'
        #assert addr_saved.password.hash == h


    def test_alias_model(self):
        mm = Alias(username='jkuralias')
        mm.created_at = datetime.now()
        mm_saved = mm.save(db)
        self.assertEqual(mm_saved.id, 1)
        self.assertEqual(mm_saved.username, 'jkuralias')

    def test_alias_model_with_ref_to_domain(self):
        alias = Alias(username='jkuralias')
        domain = Domain(name='corsario.org')
        alias.save(db)
        alias.domain = domain
        alias.save(db)
        alias.created_at = datetime.now()
        alias_saved = alias.save(db)
        self.assertEqual(alias_saved.id, 1)
        self.assertEqual(alias_saved.username, 'jkuralias')
        self.assertEqual(alias_saved.domain.name, 'corsario.org')
