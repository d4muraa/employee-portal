from flask import Blueprint, render_template
from flask_login import login_user

from app.models import User
from app.forms import LoginForm

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            return "Invalid username or password"
        login_user(user)
        return "Login succes"
    return render_template("login.html", form=form)