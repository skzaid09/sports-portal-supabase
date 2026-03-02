# # # #new3
# # # from flask import Blueprint, render_template, session, redirect

# # # admin_bp = Blueprint("admin", __name__, url_prefix="/admin")


# # # @admin_bp.route("/login")
# # # def login():
# # #     return render_template("admin/login.html")


# # # @admin_bp.route("/dashboard")
# # # def dashboard():
# # #     if "role" not in session or session["role"] != "admin":
# # #         return redirect("/admin/login")

# # #     return render_template("admin/dashboard.html")

# # #new4
# # from flask import Blueprint, render_template, session, redirect

# # admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

# # @admin_bp.route("/login")
# # def login():
# #     return render_template("admin/login.html")

# # @admin_bp.route("/dashboard")
# # def dashboard():
# #     if "user" not in session or session["user"]["role"] != "admin":
# #         return redirect("/admin/login")
# #     return render_template("admin/dashboard.html")

# # #polish
# from flask import Blueprint, render_template, session, redirect

# admin_bp = Blueprint("admin", __name__, url_prefix="/admin")


# # ADMIN LOGIN
# @admin_bp.route("/login")
# def login():
#     return render_template("admin/login.html")


# # ADMIN DASHBOARD
# @admin_bp.route("/dashboard")
# def dashboard():
#     if "user" not in session or session["user"]["role"] != "admin":
#         return redirect("/admin/login")

#     return render_template("admin/dashboard.html")

#dont know
# from flask import Blueprint, render_template, session, redirect
# import requests
# import os

# admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

# SUPABASE_URL = os.getenv("SUPABASE_URL")
# SUPABASE_KEY = os.getenv("SUPABASE_ANON_KEY")

# HEADERS = {
#     "apikey": SUPABASE_KEY,
#     "Authorization": f"Bearer {SUPABASE_KEY}"
# }

# # LOGIN
# @admin_bp.route("/login")
# def login():
#     return render_template("admin/login.html")


# # DASHBOARD
# @admin_bp.route("/dashboard")
# def dashboard():
#     if "user" not in session or session["user"]["role"] != "admin":
#         return redirect("/admin/login")

#     # 🔥 fetch players
#     players = requests.get(
#         f"{SUPABASE_URL}/rest/v1/players?select=*",
#         headers=HEADERS
#     ).json()

#     # 🔥 fetch teams
#     teams = requests.get(
#         f"{SUPABASE_URL}/rest/v1/teams?select=*",
#         headers=HEADERS
#     ).json()

#     return render_template(
#         "admin/dashboard.html",
#         players=players,
#         teams=teams
#     )


from flask import Blueprint, render_template, session, redirect
import requests
import os

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_ANON_KEY")

HEADERS = {
"apikey": SUPABASE_KEY,
"Authorization": f"Bearer {SUPABASE_KEY}"
}

# LOGIN

@admin_bp.route("/login")
def login():
    return render_template("admin/login.html")

# DASHBOARD

@admin_bp.route("/dashboard")
def dashboard():
    if "user" not in session or session["user"]["role"] != "admin":
        return redirect("/admin/login")

try:
    players = requests.get(
        f"{SUPABASE_URL}/rest/v1/players?select=*",
        headers=HEADERS
    ).json()

    teams = requests.get(
        f"{SUPABASE_URL}/rest/v1/teams?select=*",
        headers=HEADERS
    ).json()
except:
    players = []
    teams = []

return render_template(
    "admin/dashboard.html",
    players=players,
    teams=teams
)
