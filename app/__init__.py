from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///portal.db"
    
    db.init_app(app)
    
    from app import models
    
    with app.app_context():
        db.create_all()

    @app.route("/")
    def home():
        return "Employee Portal Berjalan!"
    
    return app