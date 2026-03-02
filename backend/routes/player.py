# #new3
# from flask import Blueprint, render_template, request, jsonify
# from flask import Blueprint, render_template

# player_bp = Blueprint("player", __name__)

# @player_bp.route("/options")
# def options():
#     return render_template("player/options.html")

# player_bp = Blueprint("player", __name__)

# @player_bp.route("/register")
# def register():
#     return render_template("player/register.html")

# @player_bp.route("/register/single")
# def register_single():
#     return render_template("player/register_single.html")

# @player_bp.route("/register/team")
# def register_team():
#     return render_template("player/register_team.html")


# # ✅ FIXED SINGLE PLAYER REGISTRATION
# @player_bp.route("/api/register-single", methods=["POST"])
# def api_single():
#     data = request.get_json()

#     # insert into PROFILES instead of users
#     user = supabase.table("profiles").insert({
#         "email": f"{data['roll_no']}@sports.com",
#         "role": "player"
#     }).execute()

#     if not user.data:
#         return jsonify({"error": "Profile insert failed"})

#     supabase.table("players").insert({
#         "name": data["name"],
#         "department": data["department"],
#         "roll_no": data["roll_no"],
#         "sport": data["sport"],
#         "type": "single",
#         "user_id": user.data[0]["id"]
#     }).execute()

#     return jsonify({"success": True})


# # TEAM REGISTRATION (UNCHANGED)
# @player_bp.route("/api/register-team", methods=["POST"])
# def api_team():
#     data = request.get_json()

#     team = supabase.table("teams").insert({
#         "team_name": data["team_name"],
#         "department": data["department"],
#         "sport": data["sport"]
#     }).execute()

#     for p in data["players"]:
#         supabase.table("team_players").insert({
#             "team_id": team.data[0]["id"],
#             "name": p["name"],
#             "roll_no": p["roll_no"]
#         }).execute()

#     return jsonify({"success": True})

# #polish
from flask import Blueprint, render_template, request, redirect, session, jsonify

player_bp = Blueprint("player", __name__, url_prefix="/player")


# ================= DASHBOARD =================
@player_bp.route("/dashboard")
def dashboard():
    if "user" not in session:
        return redirect("/login")

    # Fetch player registrations
    response = supabase.table("players").select("*").execute()
    players = response.data if response.data else []

    return render_template("player/dashboard.html", players=players)


# ================= SINGLE REGISTRATION =================
@player_bp.route("/api/register-single", methods=["POST"])
def register_single():
    data = request.get_json()

    supabase.table("players").insert({
        "name": data["name"],
        "sport": data["sport"],
        "type": "Single",
        "status": "Pending"
    }).execute()

    return jsonify({"success": True})