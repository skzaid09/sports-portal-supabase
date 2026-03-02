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

from flask import Blueprint, render_template, request, jsonify
from supabase import create_client
import os

coord_bp = Blueprint("coord", __name__, url_prefix="/coord")

# Supabase connection
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


# =========================
# Coordinator dashboard
# =========================
@coord_bp.route("/dashboard")
def dashboard():
    # Load matches from Supabase
    res = supabase.table("matches").select("*").execute()
    matches = res.data if res.data else []

    return render_template("coord/dashboard.html", matches=matches)


# =========================
# Save match to Supabase
# =========================
@coord_bp.route("/api/schedule-match", methods=["POST"])
def schedule_match():
    data = request.get_json()

    try:
        supabase.table("matches").insert({
            "event": data["event"],
            "team1": data["team1"],
            "team2": data["team2"],
            "date": data["date"],
            "status": "Scheduled"
        }).execute()

        return jsonify({"success": True})

    except Exception as e:
        print("MATCH ERROR:", e)
        return jsonify({"success": False})