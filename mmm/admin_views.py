from flask_admin.contrib.sqla import ModelView
from flask_admin.form import Select2Field, ImageUploadField
from flask_admin.model import typefmt
from flask_admin.actions import action
from flask_admin import BaseView, expose, AdminIndexView
from flask import current_app as app
from flask import g
from mmm import db
from datetime import datetime, timedelta
#from login import current_user


class AuthenticatedBaseView(BaseView):
    def is_accessible(self):
        return g.user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('admin.login_view', next=request.url))


class AuthenticatedView(ModelView):
    def is_accessible(self):
        return g.user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        # redirect to login page if user doesn't have access
        return redirect(url_for('admin.login_view', next=request.url))



class Account_View(AuthenticatedView):
    form_excluded_columns = ()
    form_extra_fields = {
    }
    page_size = 50
    #column_list = ('inventory_id', 'model', 'status', 'size', 'size_literal', 'framenumber', 'dateofpurchase', 'usage_days', 'bestandsmarker', 'anmerkungen')


class Domain_View(AuthenticatedView):
    form_excluded_columns = ()
    form_extra_fields = {
    }
    page_size = 50
    #column_list = ('inventory_id', 'model', 'status', 'size', 'size_literal', 'framenumber', 'dateofpurchase', 'usage_days', 'bestandsmarker', 'anmerkungen')


class Alias_View(AuthenticatedView):
    form_excluded_columns = ()
    form_extra_fields = {
    }
    page_size = 50
    #column_list = ('inventory_id', 'model', 'status', 'size', 'size_literal', 'framenumber', 'dateofpurchase', 'usage_days', 'bestandsmarker', 'anmerkungen')
