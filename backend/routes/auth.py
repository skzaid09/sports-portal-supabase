# #new3
# from flask import Blueprint, request, jsonify, session

# auth_bp = Blueprint("auth", __name__)

# # SIMPLE LOGIN (NO SUPABASE FOR DEMO)
# @auth_bp.route("/api/login", methods=["POST"])
# def login():
#     data = request.get_json()
#     email = data.get("email")
#     password = data.get("password")
#     role = data.get("role")

#     # 🔥 SIMPLE DEMO LOGIC
#     if role == "admin" and password == "admin123":
#         session["user"] = {"email": email, "role": "admin"}
#         return jsonify({
#             "success": True,
#             "redirect": "/admin/dashboard"
#         })

#     elif role == "coord" and password == "coord123":
#         session["user"] = {"email": email, "role": "coord"}
#         return jsonify({
#             "success": True,
#             "redirect": "/coord/dashboard"
#         })

#     else:
#         return jsonify({
#             "success": False,
#             "message": "Invalid credentials"
#         })

#new4
from flask import Blueprint, request, jsonify, session

auth_bp = Blueprint("auth", __name__)

# SIMPLE DEMO LOGIN API
@auth_bp.route("/api/login", methods=["POST"])
def login():
    data = request.get_json()

    email = data.get("email")
    password = data.get("password")
    role = data.get("role")

    # -------- SIMPLE DEMO LOGIC -------- #

    # ADMIN LOGIN
    if role == "admin" and password == "admin123":
        session["user"] = {
            "email": email,
            "role": "admin"
        }
        return jsonify({
            "success": True,
            "redirect": "/admin/dashboard"
        })

    # COORD LOGIN
    if role == "coord" and password == "coord123":
        session["user"] = {
            "email": email,
            "role": "coord"
        }
        return jsonify({
            "success": True,
            "redirect": "/coord/dashboard"
        })

    return jsonify({
        "success": False,
        "message": "Invalid email or role"
    })


# LOGOUT (important for your habit 😎)
@auth_bp.route("/logout")
def logout():
    session.clear()
    return jsonify({"success": True})