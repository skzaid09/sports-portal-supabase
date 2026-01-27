from flask import Blueprint, request, jsonify, session
from config import supabase

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/api/login", methods=["POST"])
def login():
    try:
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")
        role = data.get("role")

        auth_res = supabase.auth.sign_in_with_password({
            "email": email,
            "password": password
        })

        if not auth_res.session:
            return jsonify({"success": False, "message": "Invalid credentials"}), 401

        prof = supabase.table("users").select("role").eq("email", email).execute()

        if not prof.data or prof.data[0]["role"] != role:
            return jsonify({"success": False, "message": "Role mismatch"}), 401

        session["user"] = {"email": email, "role": role}

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
