from flask import Blueprint
from flask_login import current_user, login_required

from app.models import Payslip

employee_bp = Blueprint("employee", __name__)


@employee_bp.route("/payslip/<int:payslip_id>")
@login_required
def payslip(payslip_id):
    slip = Payslip.query.filter_by(
        id=payslip_id, user_id=current_user.id
    ).first_or_404()
    return f"Payslip {slip.period}: {slip.amount}"