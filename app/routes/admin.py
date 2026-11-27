from flask import Blueprint

from app.utils.decorators import role_required

admin_bp = Blueprint("admin", __name__)


@admin_bp.route("/admin")
@role_required("admin")
def dashboard():
    return "Admin area"