# coding: utf-8
from flask_admin import Admin
from mmm.models import Account, Domain, Alias

def register_admin(app, db):
    with app.app_context():
        from mmm.admin_views import Account_View, Alias_View, Domain_View
        admin = Admin(app, name='MMM Admin', template_mode='bootstrap3')
        #admin.add_view(Bike_Type_View(Bike_Type, db.session, name='Fahrradmodelle'))
        admin.add_view(Account_View(Account, db.session, name='Accounts'))
        admin.add_view(Domain_View(Domain, db.session, name='Domains'))
        admin.add_view(Alias_View(Alias, db.session, name='Aliases'))
