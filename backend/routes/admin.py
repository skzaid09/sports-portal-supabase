# # #new3
# # from flask import Blueprint, render_template, session, redirect

# # admin_bp = Blueprint("admin", __name__, url_prefix="/admin")


# # @admin_bp.route("/login")
# # def login():
# #     return render_template("admin/login.html")


# # @admin_bp.route("/dashboard")
# # def dashboard():
# #     if "role" not in session or session["role"] != "admin":
# #         return redirect("/admin/login")

# #     return render_template("admin/dashboard.html")

# #new4
# from flask import Blueprint, render_template, session, redirect

# admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

# @admin_bp.route("/login")
# def login():
#     return render_template("admin/login.html")

# @admin_bp.route("/dashboard")
# def dashboard():
#     if "user" not in session or session["user"]["role"] != "admin":
#         return redirect("/admin/login")
#     return render_template("admin/dashboard.html")

# #polish
from flask import Blueprint, render_template, session, redirect

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")


@admin_bp.route("/dashboard")
def dashboard():
    if "user" not in session or session["user"]["role"] != "admin":
        return redirect("/admin/login")

    # Fetch users
    users = supabase.table("profiles").select("*").execute().data

    # Fetch registrations
    players = supabase.table("players").select("*").execute().data

    return render_template("admin/dashboard.html",
                           users=users,
                           players=players)