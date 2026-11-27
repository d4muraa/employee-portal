from app import create_app, db
from app.models import Payslip, User

app = create_app()

SAMPLE_PAYSLIPS = [
    ("Daffa", "2026-10", 8000000),
    ("Daffa", "2026-11", 8000000),
    ("Budi", "2026-10", 8000000),
    ("Budi", "2026-11", 8000000),
]

with app.app_context():
    for username, period, amount in SAMPLE_PAYSLIPS:
        user = User.query.filter_by(username=username).first()
        if user is None:
            print(f"Skipped: user '{username}' not found.")
            continue
        db.session.add(Payslip(user_id=user.id, period=period, amount=amount))
    db.session.commit()
    print("Sample payslips created.")