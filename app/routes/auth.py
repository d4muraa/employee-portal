from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import login_user, login_required, logout_user

from app.models import User
from app.utils.audit import log_action
from app.forms import LoginForm

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.check_password(form.password.data):
            login_user(user)
            log_action("auth.login.success", "success")
            return redirect(url_for("home"))
        log_action("auth.login.failure", "failure", reason_code="invalid_credentials")
        flash("Invalid username or password")
    return render_template("login.html", form=form)

@auth_bp.route("/logout", methods=["POST"])
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))