from getpass import getpass

from app import create_app, db
from app.models import User

app = create_app()

with app.app_context():
    username = input("Username: ")
    password = getpass("Password:")
    role = input("Role (employee/hr/admin) [employee]: ") or "employee"
    
    if role not in ("employee", "hr", "admin"):
        raise SystemExit("Invalid role.")
    
    user = User(username=username, role=role)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    print(f"User '{username}' created with role '{role}'.")