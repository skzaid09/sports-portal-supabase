from flask import Blueprint, request, jsonify, session
from config import supabase

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/api/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")
    role = data.get("role")

    try:
        auth = supabase.auth.sign_in_with_password({
            "email": email,
            "password": password
        })

        user = supabase.table("users").select("role").eq("email", email).execute()

        if user.data and user.data[0]["role"] == role:
            session["user"] = {"email": email, "role": role}
            return jsonify({"success": True, "redirect": f"/{role}/dashboard"})

        return jsonify({"success": False, "message": "Invalid role"}), 401

    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

@auth_bp.route("/api/logout", methods=["POST"])
def logout():
    session.clear()
    return jsonify({"success": True})
