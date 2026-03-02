# # #new3
# # from flask import Blueprint, render_template, session, redirect

# # coord_bp = Blueprint("coord", __name__, url_prefix="/coord")


# # @coord_bp.route("/login")
# # def login():
# #     return render_template("coord/login.html")


# # @coord_bp.route("/dashboard")
# # def dashboard():
# #     if "role" not in session or session["role"] != "coord":
# #         return redirect("/coord/login")

# #     return render_template("coord/dashboard.html")

# #new4
# # from flask import Blueprint, render_template, session, redirect

# # coord_bp = Blueprint("coord", __name__, url_prefix="/coord")

# # @coord_bp.route("/login")
# # def login():
# #     return render_template("coord/login.html")

# # @coord_bp.route("/dashboard")
# # def dashboard():
# #     if "user" not in session or session["user"]["role"] != "coord":
# #         return redirect("/coord/login")
# #     return render_template("coord/dashboard.html")

# #polish
# from flask import Blueprint, render_template, session, redirect

# coord_bp = Blueprint("coord", __name__, url_prefix="/coord")


# # COORD LOGIN
# @coord_bp.route("/login")
# def login():
#     return render_template("coord/login.html")


# # COORD DASHBOARD
# @coord_bp.route("/dashboard")
# def dashboard():
#     if "user" not in session or session["user"]["role"] != "coord":
#         return redirect("/coord/login")

#     return render_template("coord/dashboard.html")

from flask import Blueprint, render_template, session, redirect, request, jsonify
import requests
import os

coord_bp = Blueprint("coord", __name__, url_prefix="/coord")

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_ANON_KEY")

HEADERS = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}"
}

@coord_bp.route("/login")
def login():
    return render_template("coord/login.html")


@coord_bp.route("/dashboard")
def dashboard():
    if "user" not in session or session["user"]["role"] != "coord":
        return redirect("/coord/login")

    matches = requests.get(
        f"{SUPABASE_URL}/rest/v1/matches?select=*",
        headers=HEADERS
    ).json()

    return render_template("coord/dashboard.html", matches=matches)


# schedule match
@coord_bp.route("/api/match", methods=["POST"])
def create_match():
    data = request.json

    res = requests.post(
        f"{SUPABASE_URL}/rest/v1/matches",
        json=data,
        headers=HEADERS
    )

    return jsonify({"success": True})