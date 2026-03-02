# from flask import Blueprint, request, session, redirect, url_for, render_template
# from config import supabase

# auth_bp = Blueprint("auth", __name__)

# @auth_bp.route("/login", methods=["GET", "POST"])
# def login():
#     if request.method == "POST":
#         email = request.form["email"]
#         password = request.form["password"]

#         try:
#             # Supabase login
#             result = supabase.auth.sign_in_with_password({
#                 "email": email,
#                 "password": password
#             })

#             user_id = result.user.id

#             # Get role from profiles table
#             profile = supabase.table("profiles") \
#                 .select("*") \
#                 .eq("id", user_id) \
#                 .execute()

#             if not profile.data:
#                 return "User role not found!"

#             role = profile.data[0]["role"]

#             session["user_id"] = user_id
#             session["role"] = role

#             role = role.lower().strip()

#             if role == "admin":
#                 return redirect("/admin/dashboard")
#             elif role in ["coord", "coordinator"]:
#                 return redirect("/coord/dashboard")

#             else:
#                 return "Role not configured"

#         except Exception as e:
#             return f"Login error: {str(e)}"

#     return render_template("login.html")


# @auth_bp.route("/logout")
# def logout():
#     session.clear()
#     return redirect(url_for("auth.login"))
from flask import jsonify

@auth_bp.route("/api/login", methods=["POST"])
def api_login():
    data = request.get_json()

    email = data.get("email")
    password = data.get("password")

    try:
        # Supabase login
        result = supabase.auth.sign_in_with_password({
            "email": email,
            "password": password
        })

        user_id = result.user.id

        # get role
        profile = supabase.table("profiles") \
            .select("*") \
            .eq("id", user_id) \
            .execute()

        if not profile.data:
            return jsonify({"error": "Role not found"}), 400

        role = profile.data[0]["role"]

        return jsonify({
            "success": True,
            "role": role
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400