# backend/routes/auth.py
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
        # 1️⃣ Authenticate with Supabase Auth
        auth = supabase.auth.sign_in_with_password({
            "email": email,
            "password": password
        })

        user = auth.user
        if not user:
            return jsonify({"success": False, "message": "Invalid credentials"}), 401

        # 2️⃣ Fetch role from profiles table
        profile = supabase.table("profiles") \
            .select("role") \
            .eq("id", user.id) \
            .single() \
            .execute()

        if not profile.data:
            return jsonify({"success": False, "message": "Profile not found"}), 403

        if profile.data["role"] != role:
            return jsonify({"success": False, "message": "Role mismatch"}), 403

        # 3️⃣ Save session
        session["user"] = {
            "id": user.id,
            "email": email,
            "role": role
        }

        return jsonify({
            "success": True,
            "redirect": f"/{role}/dashboard"
        })

    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500


@auth_bp.route("/api/logout", methods=["POST"])
def logout():
    session.clear()
    return jsonify({"success": True})
