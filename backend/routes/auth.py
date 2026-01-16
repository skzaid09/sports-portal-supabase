from flask import Blueprint, request, jsonify, session
from config import supabase

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/api/login", methods=["POST"])
def login():
    data = request.json
    email = data["email"]
    password = data["password"]
    role = data["role"]

    res = supabase.auth.sign_in_with_password({
        "email": email,
        "password": password
    })

    user = supabase.table("users").select("role").eq("email", email).execute()

    if user.data and user.data[0]["role"] == role:
        session["user"] = {"email": email, "role": role}
        return jsonify(success=True, redirect=f"/{role}/dashboard")

    return jsonify(success=False, message="Invalid login")
