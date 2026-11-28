from flask import Blueprint, abort, flash, redirect, render_template, url_for
from flask_login import current_user

from app import db
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


@admin_bp.route("/admin/leaves/<int:leave_id>/approve", methods=["POST"])
@role_required("hr", "admin")
def approve_leave(leave_id):
    leave = db.session.get(LeaveRequest, leave_id)
    if leave is None:
        abort(404)
    if leave.user_id == current_user.id:
        abort(403)
    if leave.status != "pending":
        flash("Pengajuan ini sudah diproses.")
        return redirect(url_for("admin.list_leaves"))
    leave.status = "approved"
    db.session.commit()
    flash("Pengajuan cuti disetujui.")
    return redirect(url_for("admin.list_leaves"))