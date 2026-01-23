# backend/routes/auth.py
from flask import Blueprint, request, jsonify, session
from config import supabase

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

        # Validate email format
        if '@' not in email:
            return jsonify({"success": False, "message": "Invalid email format"}), 400

        # Sign in with Supabase Auth
        auth_response = supabase.auth.sign_in_with_password({
            "email": email,
            "password": password
        })

        if auth_response.session:
            # Verify role from profiles table
            profile_response = supabase.table('profiles').select('role').eq('email', email).execute()
            
            if not profile_response.data:
                return jsonify({"success": False, "message": "User not found in profiles"}), 401
                
            if profile_response.data[0]['role'] == role:
                session['user'] = {
                    'email': email,
                    'role': role
                }
                return jsonify({
                    "success": True,
                    "redirect": f"/{role}/dashboard"
                })
            else:
                return jsonify({"success": False, "message": "Invalid role"}), 401
        else:
            return jsonify({"success": False, "message": "Invalid credentials"}), 401

    except Exception as e:
        return jsonify({"success": False, "message": f"Server error: {str(e)}"}), 500# backend/routes/auth.py
from flask import Blueprint, request, jsonify, session
from config import supabase

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

        # Validate email format
        if '@' not in email:
            return jsonify({"success": False, "message": "Invalid email format"}), 400

        # Sign in with Supabase Auth
        auth_response = supabase.auth.sign_in_with_password({
            "email": email,
            "password": password
        })

        if auth_response.session:
            # Verify role from profiles table
            profile_response = supabase.table('profiles').select('role').eq('email', email).execute()
            
            if not profile_response.data:
                return jsonify({"success": False, "message": "User not found in profiles"}), 401
                
            if profile_response.data[0]['role'] == role:
                session['user'] = {
                    'email': email,
                    'role': role
                }
                return jsonify({
                    "success": True,
                    "redirect": f"/{role}/dashboard"
                })
            else:
                return jsonify({"success": False, "message": "Invalid role"}), 401
        else:
            return jsonify({"success": False, "message": "Invalid credentials"}), 401

    except Exception as e:
        return jsonify({"success": False, "message": f"Server error: {str(e)}"}), 500