# coding: utf-8
from flask_admin import Admin
from mmm.models import Account, Domain, Alias

def register_admin(app, db):
    with app.app_context():
        #from mmm.admin.views import Alias_View
        admin = Admin(app, name='Mega MailManager', template_mode='bootstrap3')
        #admin.add_view(Bike_Type_View(Bike_Type, db.session, name='Fahrradmodelle'))
