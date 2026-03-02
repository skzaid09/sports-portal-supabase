# from flask import Blueprint, render_template, session, redirect
# from flask import Blueprint, render_template

# admin_bp = Blueprint("admin", __name__)

# @admin_bp.route("/dashboard")
# def dashboard():
#     return render_template("admin/dashboard.html")

# admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

# @admin_bp.route("/login")
# def login():
#     return render_template("admin/login.html")

# @admin_bp.route("/dashboard")
# def dashboard():
#     if "user" not in session or session["user"]["role"] != "admin":
#         return redirect("/admin/login")
#     return render_template("admin/dashboard.html")

from flask import Blueprint, render_template, session, redirect

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")


@admin_bp.route("/login")
def login():
    return render_template("admin/login.html")


@admin_bp.route("/dashboard")
def dashboard():
    if "role" not in session or session["role"] != "admin":
        return redirect("/admin/login")

    return render_template("admin/dashboard.html")