
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from mmm.models import Domain


def domain_query_factory():
    return Domain.query

class DomainField(QuerySelectField):
    def __init__(self, *args, **kwargs):
        super(DomainField, self).__init__(query_factory=domain_query_factory, get_label='name', allow_blank=True, **kwargs)

