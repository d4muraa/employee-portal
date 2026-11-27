from getpass import getpass

from app import create_app, db
from app.models import User

app = create_app()

with app.app_context():
    username = input("Username: ")
    user = User.query.filter_by(username=username).first()
    if user is None:
        raise SystemExit("User not found.")
    
    password = getpass("New password: ")
    confirm = getpass("Repeat new password: ")
    if password != confirm:
        raise SystemExit("Passwords do not match.")
    
    user.set_password(password)
    db.session.commit()
    print(f"Password updated for '{username}'")