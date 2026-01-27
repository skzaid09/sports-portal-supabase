from flask import Blueprint, render_template, request, jsonify
from supabase_client import supabase

player_bp = Blueprint("player", __name__, url_prefix="/player")

@player_bp.route("/register")
def register():
    return render_template("player/register.html")

@player_bp.route("/register/single")
def single():
    return render_template("player/register_single.html")

@player_bp.route("/register/team")
def team():
    return render_template("player/register_team.html")

@player_bp.route("/dashboard")
def dashboard():
    return render_template("player/dashboard.html")

@player_bp.route("/api/register-single", methods=["POST"])
def api_register_single():
    data = request.json
    supabase.table("players").insert(data).execute()
    return jsonify({"success": True})

@player_bp.route("/api/register-team", methods=["POST"])
def api_register_team():
    data = request.json
    team = supabase.table("teams").insert({
        "team_name": data["team_name"],
        "department": data["department"],
        "sport": data["sport"]
    }).execute()
    
    team_id = team.data[0]["id"]
    for p in data["players"]:
        supabase.table("team_players").insert({
            "team_id": team_id,
            "name": p["name"],
            "roll_no": p["roll_no"]
        }).execute()
    
    return jsonify({"success": True})
