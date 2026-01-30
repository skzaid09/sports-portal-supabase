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
        # 1️⃣ Supabase Auth Login
        auth_res = supabase.auth.sign_in_with_password({
            "email": email,
            "password": password
        })

        if not auth_res.user:
            return jsonify({"success": False, "message": "Invalid credentials"}), 401

        # 2️⃣ Fetch role from public.users
        user_res = supabase.table("users").select("role").eq("email", email).execute()

        if not user_res.data:
            return jsonify({"success": False, "message": "User role not found"}), 403

        db_role = user_res.data[0]["role"]

        if db_role != role:
            return jsonify({"success": False, "message": "Role mismatch"}), 403

        # 3️⃣ Save session
        session["user"] = {
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
