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
        # 1️⃣ Authenticate user via Supabase Auth
        auth_res = supabase.auth.sign_in_with_password({
            "email": email,
            "password": password
        })

        if not auth_res.user:
            return jsonify({"success": False, "message": "Invalid credentials"}), 401

        # 2️⃣ Fetch role from users table
        user_res = (
            supabase
            .table("users")
            .select("role")
            .eq("email", email)
            .single()
            .execute()
        )

        if not user_res.data or user_res.data["role"] != role:
            return jsonify({"success": False, "message": "Unauthorized role"}), 403

        # 3️⃣ Store session
        session["user"] = {
            "email": email,
            "role": role
        }

        return jsonify({
            "success": True,
            "redirect": f"/{role}/dashboard"
        })

    except Exception as e:
        print("LOGIN ERROR:", e)
        return jsonify({"success": False, "message": "Login failed"}), 500


@auth_bp.route("/api/logout", methods=["POST"])
def logout():
    session.clear()
    return jsonify({"success": True})
