from flask import Blueprint, request, jsonify, session
from config import supabase

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/api/login", methods=["POST"])
def login():
    data = request.get_json()

    email = data.get("email")
    password = data.get("password")
    role = data.get("role")

    if not email or not password or not role:
        return jsonify({"success": False, "message": "Missing fields"}), 400

    try:
        # Supabase Auth Login
        res = supabase.auth.sign_in_with_password({
            "email": email,
            "password": password
        })

        # Get role from users table
        user = supabase.table("users").select("role").eq("email", email).single().execute()

        if not user.data:
            return jsonify({"success": False, "message": "User not found"}), 404

        if user.data["role"] != role:
            return jsonify({"success": False, "message": "Invalid role"}), 403

        session["user"] = {
            "email": email,
            "role": role
        }

        return jsonify({"success": True, "redirect": f"/{role}/dashboard"})

    except Exception as e:
        print("LOGIN ERROR:", e)
        return jsonify({"success": False, "message": "Login failed"}), 500


@auth_bp.route("/api/logout", methods=["POST"])
def logout():
    session.clear()
    return jsonify({"success": True})
