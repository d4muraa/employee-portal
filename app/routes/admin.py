from flask import Blueprint, render_template

from app.utils.decorators import role_required
from app.models import LeaveRequest

admin_bp = Blueprint("admin", __name__)


@admin_bp.route("/admin")
@role_required("admin")
def dashboard():
    return "Admin area"


@admin_bp.route("/admin/leaves")
@role_required("hr", "admin")
def list_leaves():
    leaves = LeaveRequest.query.order_by(LeaveRequest.id.desc()).all()
    return render_template("leave_list.html", leaves=leaves)