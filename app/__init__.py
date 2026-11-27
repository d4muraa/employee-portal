import os

from dotenv import load_dotenv
from flask import Flask, render_template
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

load_dotenv()

db = SQLAlchemy()
login_manager = LoginManager()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    
    secret_key = os.environ.get("SECRET_KEY")
    if not secret_key:
        raise RuntimeError(
            "SECRET_KEY is not set. Copy .env.example to .env and fill it in."
        )
    app.config["SECRET_KEY"] = secret_key
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///portal.db"
    
    db.init_app(app)
    login_manager.init_app(app)
    csrf.init_app(app)
    login_manager.login_view = "auth.login"
    
    from app import models
    
    with app.app_context():
        db.create_all()
    
    from app.routes.auth import auth_bp
    app.register_blueprint(auth_bp)
    from app.routes.admin import admin_bp
    app.register_blueprint(admin_bp)
    
    @app.route("/")
    def home():
        return render_template("home.html")
    
    return app