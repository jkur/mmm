from flask import current_app as app
from flask import request, flash, redirect, session
from flask import Blueprint, render_template, redirect, url_for
from .forms import Domain_Form, Account_Form
from .models import Domain, Account, Alias
from mmm import db
from mmm.services import login_user_from_db
#from flask_user import logout_user


mod = Blueprint('views', __name__)

@mod.route("/")
def index():
    return render_template("index.html")

@mod.route("/domain", methods=['GET', 'POST'])
def domain():
    form = Domain_Form(request.form)
    if form.validate_on_submit():
        d = Domain()
        form.populate_obj(d)
        d.save(db)
        flash("saved")
        return redirect(url_for('.domain'))
    domains = Domain.query.all()
    return render_template("domain/add.html", domainform=form, domains=domains)


@mod.route("/aliases", methods=['GET', 'POST'])
def aliases():
    form = Domain_Form(request.form)
    if form.validate_on_submit():
        d = Domain()
        form.populate_obj(d)
        d.save(db)
        # flash("saved")
        return redirect(url_for('.aliases'))
    domains = Domain.query.all()
    return render_template("domain/add.html", domainform=form)


#@mod.route("/address/<id>", methods=['DELETE'])
#def delete_addresses(id):
#    addr = Account.query.get_or_404(id)
#    db.session.delete(addr)
#    db.session.commit()
#    return redirect(url_for('.addresses'))


@mod.route("/address", methods=['GET', 'POST'])
def addresses():
    form = Account_Form(request.form)
    print("request.form", request.form)
    print(form.__dict__)
    if form.validate_on_submit():
        d = Account()
        form.populate_obj(d)
        d.save(db)
        flash("saved")
        return redirect(url_for('.addresses'))
    else:
        print("form:\n ", dir(form.domain))
        print("validation failed")
    addresses = Account.query.all()
    return render_template("address/edit.html",
                           addressform=form,
                           addresses=addresses)
