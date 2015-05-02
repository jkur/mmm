from tests import MMMTestCase

from mmm.models import Domain
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

        
