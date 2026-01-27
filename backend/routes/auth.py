# backend/routes/auth.py
from flask import Blueprint, request, jsonify, session
from models.user import get_user_by_email

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/api/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')
        role = data.get('role')

        if not email or not password or not role:
            return jsonify({"success": False, "message": "Missing fields"}), 400

        # Verify credentials using Supabase Auth
        try:
            auth_response = supabase.auth.sign_in_with_password({
                "email": email,
                "password": password
            })
        except Exception as e:
            return jsonify({"success": False, "message": "Invalid credentials"}), 401

        # Get user role
        user = get_user_by_email(email)
        if not user:
            return jsonify({"success": False, "message": "User not found"}), 401

        if user['role'] != role:
            return jsonify({"success": False, "message": "Invalid role"}), 401

        session['user'] = {
            'email': email,
            'role': role
        }
        return jsonify({
            "success": True,
            "redirect": f"/{role}/dashboard"
        })

    except Exception as e:
        return jsonify({"success": False, "message": f"Server error: {str(e)}"}), 500