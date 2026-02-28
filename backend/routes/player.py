from flask import Blueprint, request, jsonify
from config import supabase

player_bp = Blueprint("player", __name__)

@player_bp.route("/api/register-single", methods=["POST"])
def register_single():
    data = request.get_json()

    try:
        # Step 1: create auth user
        auth_user = supabase.auth.admin.create_user({
            "email": f"{data['roll_no']}@sports.com",
            "password": "default123"
        })

        user_id = auth_user.user.id

        # Step 2: add role in profiles
        supabase.table("profiles").insert({
            "id": user_id,
            "email": auth_user.user.email,
            "role": "player"
        }).execute()

        # Step 3: insert player
        supabase.table("players").insert({
            "name": data["name"],
            "department": data["department"],
            "roll_no": data["roll_no"],
            "sport": data["sport"],
            "type": "single",
            "user_id": user_id
        }).execute()

        return jsonify({"success": True})

    except Exception as e:
        return jsonify({"error": str(e)})