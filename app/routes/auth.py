from flask import Blueprint, render_template
from app.forms import LoginForm

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login")
def login():
    form = LoginForm()
    return render_template("login.html", form=form)