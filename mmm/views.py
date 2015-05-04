from flask import current_app as app
from flask import request
from flask import Blueprint, render_template, redirect, url_for

from .forms import Domain_Form

mod = Blueprint('views', __name__)

@mod.route("/")
def index():
    return "index"


@mod.route("/domain/new", methods=['GET', 'POST'])
def domain_add():
    form = Domain_Form(request.form)
    if form.validate_on_submit():
        return redirect(url_for('.index'))
    return render_template("domain/add.html", domainform=form)
