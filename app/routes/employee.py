from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import current_user, login_required

from app import db
from app.forms import LeaveForm
from app.models import LeaveRequest, Payslip

employee_bp = Blueprint("employee", __name__)


@employee_bp.route("/payslip/<int:payslip_id>")
@login_required
def payslip(payslip_id):
    slip = Payslip.query.filter_by(
        id=payslip_id, user_id=current_user.id
    ).first_or_404()
    return f"Payslip {slip.period}: {slip.amount}"


@employee_bp.route("/leave/new", methods=["GET", "POST"])
@login_required
def new_leave():
    form = LeaveForm()
    if form.validate_on_submit():
        leave = LeaveRequest(
            user_id=current_user.id,
            start_date=form.start_date.data,
            end_date=form.end_date.data,
            reason=form.reason.data,
        )
        db.session.add(leave)
        db.session.commit()
        flash("Pengajuan cuti terkirim.")
        return redirect(url_for("home"))
    return render_template("leave_form.html", form=form)