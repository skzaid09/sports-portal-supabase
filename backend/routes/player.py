from flask import Blueprint, render_template, request, jsonify
from config import supabase

player_bp = Blueprint("player", __name__)

@player_bp.route("/register")
def register():
    return render_template("player/register.html")

@player_bp.route("/api/register-single", methods=["POST"])
def register_single():
    data = request.json
    supabase.table("players").insert(data).execute()
    return jsonify(success=True)
