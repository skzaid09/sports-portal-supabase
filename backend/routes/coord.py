# #new3
# from flask import Blueprint, render_template, session, redirect

# coord_bp = Blueprint("coord", __name__, url_prefix="/coord")


# @coord_bp.route("/login")
# def login():
#     return render_template("coord/login.html")


# @coord_bp.route("/dashboard")
# def dashboard():
#     if "role" not in session or session["role"] != "coord":
#         return redirect("/coord/login")

#     return render_template("coord/dashboard.html")

#new4
# from flask import Blueprint, render_template, session, redirect

# coord_bp = Blueprint("coord", __name__, url_prefix="/coord")

# @coord_bp.route("/login")
# def login():
#     return render_template("coord/login.html")

# @coord_bp.route("/dashboard")
# def dashboard():
#     if "user" not in session or session["user"]["role"] != "coord":
#         return redirect("/coord/login")
#     return render_template("coord/dashboard.html")

#polish
from flask import Blueprint, render_template, request, redirect, session, jsonify

coord_bp = Blueprint("coord", __name__, url_prefix="/coord")


# ================= DASHBOARD =================
@coord_bp.route("/dashboard")
def dashboard():
    if "user" not in session or session["user"]["role"] != "coord":
        return redirect("/coord/login")

    # Fetch matches from Supabase
    response = supabase.table("matches").select("*").execute()
    matches = response.data if response.data else []

    return render_template("coord/dashboard.html", matches=matches)


# ================= SCHEDULE MATCH =================
@coord_bp.route("/api/schedule-match", methods=["POST"])
def schedule_match():
    data = request.get_json()

    supabase.table("matches").insert({
        "event": data["event"],
        "team1": data["team1"],
        "team2": data["team2"],
        "date": data["date"],
        "status": "Scheduled"
    }).execute()

    return jsonify({"success": True})