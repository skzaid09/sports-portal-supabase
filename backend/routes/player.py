from flask import Blueprint, render_template, request, jsonify
from config import supabase

player_bp = Blueprint("player", __name__)

@player_bp.route("/register")
def register():
    return render_template("player/register.html")

@player_bp.route("/register/single")
def register_single():
    return render_template("player/register_single.html")

@player_bp.route("/register/team")
def register_team():
    return render_template("player/register_team.html")

@player_bp.route("/api/register-single", methods=["POST"])
def api_single():
    data = request.get_json()

    user = supabase.table("users").insert({
        "email": f"{data['roll_no']}@sports.com",
        "role": "player"
    }).execute()

    supabase.table("players").insert({
        "name": data["name"],
        "department": data["department"],
        "roll_no": data["roll_no"],
        "sport": data["sport"],
        "type": "single",
        "user_id": user.data[0]["id"]
    }).execute()

    return jsonify({"success": True})

@player_bp.route("/api/register-team", methods=["POST"])
def api_team():
    data = request.get_json()

    team = supabase.table("teams").insert({
        "team_name": data["team_name"],
        "department": data["department"],
        "sport": data["sport"]
    }).execute()

    for p in data["players"]:
        supabase.table("team_players").insert({
            "team_id": team.data[0]["id"],
            "name": p["name"],
            "roll_no": p["roll_no"]
        }).execute()

    return jsonify({"success": True})
