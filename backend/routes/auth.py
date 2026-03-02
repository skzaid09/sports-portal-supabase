# # # # # # # # from flask import Blueprint, request, session, redirect, url_for, render_template
# # # # # # # # from config import supabase

# # # # # # # # auth_bp = Blueprint("auth", __name__)

# # # # # # # # @auth_bp.route("/login", methods=["GET", "POST"])
# # # # # # # # def login():
# # # # # # # #     if request.method == "POST":
# # # # # # # #         email = request.form["email"]
# # # # # # # #         password = request.form["password"]

# # # # # # # #         try:
# # # # # # # #             # Supabase login
# # # # # # # #             result = supabase.auth.sign_in_with_password({
# # # # # # # #                 "email": email,
# # # # # # # #                 "password": password
# # # # # # # #             })

# # # # # # # #             user_id = result.user.id

# # # # # # # #             # Get role from profiles table
# # # # # # # #             profile = supabase.table("profiles") \
# # # # # # # #                 .select("*") \
# # # # # # # #                 .eq("id", user_id) \
# # # # # # # #                 .execute()

# # # # # # # #             if not profile.data:
# # # # # # # #                 return "User role not found!"

# # # # # # # #             role = profile.data[0]["role"]

# # # # # # # #             session["user_id"] = user_id
# # # # # # # #             session["role"] = role

# # # # # # # #             role = role.lower().strip()

# # # # # # # #             if role == "admin":
# # # # # # # #                 return redirect("/admin/dashboard")
# # # # # # # #             elif role in ["coord", "coordinator"]:
# # # # # # # #                 return redirect("/coord/dashboard")

# # # # # # # #             else:
# # # # # # # #                 return "Role not configured"

# # # # # # # #         except Exception as e:
# # # # # # # #             return f"Login error: {str(e)}"

# # # # # # # #     return render_template("login.html")


# # # # # # # # @auth_bp.route("/logout")
# # # # # # # # def logout():
# # # # # # # #     session.clear()
# # # # # # # #     return redirect(url_for("auth.login"))

# # # # # # # 222
# # # # # # # from flask import Blueprint, request, jsonify, render_template, redirect, session
# # # # # # # from config import supabase

# # # # # # # # ✅ CREATE BLUEPRINT FIRST (THIS WAS MISSING)
# # # # # # # auth_bp = Blueprint("auth", __name__)


# # # # # # # # =============================
# # # # # # # # LOGIN PAGE
# # # # # # # # =============================
# # # # # # # @auth_bp.route("/login")
# # # # # # # def login_page():
# # # # # # #     return render_template("login.html")


# # # # # # # # =============================
# # # # # # # # API LOGIN (FOR AJAX)
# # # # # # # # =============================
# # # # # # # @auth_bp.route("/api/login", methods=["POST"])
# # # # # # # def api_login():
# # # # # # #     data = request.get_json()

# # # # # # #     email = data.get("email")
# # # # # # #     password = data.get("password")

# # # # # # #     try:
# # # # # # #         # Supabase login
# # # # # # #         result = supabase.auth.sign_in_with_password({
# # # # # # #             "email": email,
# # # # # # #             "password": password
# # # # # # #         })

# # # # # # #         user_id = result.user.id

# # # # # # #         # Fetch role
# # # # # # #         profile = supabase.table("profiles") \
# # # # # # #             .select("*") \
# # # # # # #             .eq("id", user_id) \
# # # # # # #             .execute()

# # # # # # #         if not profile.data:
# # # # # # #             return jsonify({
# # # # # # #                 "success": False,
# # # # # # #                 "message": "Role not found"
# # # # # # #             })

# # # # # # #         role = profile.data[0]["role"]

# # # # # # #         # Save session (good for security + viva)
# # # # # # #         session["user_id"] = user_id
# # # # # # #         session["role"] = role

# # # # # # #         # Redirect based on role
# # # # # # #         if role == "admin":
# # # # # # #             redirect_url = "/admin/dashboard"
# # # # # # #         elif role in ["coord", "coordinator"]:
# # # # # # #             redirect_url = "/coord/dashboard"
# # # # # # #         else:
# # # # # # #             return jsonify({
# # # # # # #                 "success": False,
# # # # # # #                 "message": "Invalid role"
# # # # # # #             })

# # # # # # #         return jsonify({
# # # # # # #             "success": True,
# # # # # # #             "redirect": redirect_url
# # # # # # #         })

# # # # # # #     except Exception as e:
# # # # # # #         return jsonify({
# # # # # # #             "success": False,
# # # # # # #             "message": str(e)
# # # # # # #         })


# # # # # # # # =============================
# # # # # # # # LOGOUT
# # # # # # # # =============================
# # # # # # # @auth_bp.route("/logout")
# # # # # # # def logout():
# # # # # # #     session.clear()
# # # # # # #     return redirect("/login")
# # # # # # #333

# # # # # # from flask import Blueprint, request, jsonify, render_template, redirect, session
# # # # # # from config import supabase

# # # # # # # ✅ CREATE BLUEPRINT FIRST (THIS WAS MISSING)
# # # # # # auth_bp = Blueprint("auth", __name__)


# # # # # # # =============================
# # # # # # # LOGIN PAGE
# # # # # # # =============================
# # # # # # @auth_bp.route("/login")
# # # # # # def login_page():
# # # # # #     return render_template("login.html")


# # # # # # # =============================
# # # # # # # API LOGIN (FOR AJAX)
# # # # # # # =============================
# # # # # # @auth_bp.route("/api/login", methods=["POST"])
# # # # # # def api_login():
# # # # # #     data = request.get_json()

# # # # # #     email = data.get("email")
# # # # # #     password = data.get("password")

# # # # # #     try:
# # # # # #         # Supabase login
# # # # # #         result = supabase.auth.sign_in_with_password({
# # # # # #             "email": email,
# # # # # #             "password": password
# # # # # #         })

# # # # # #         user_id = result.user.id

# # # # # #         # Fetch role
# # # # # #         profile = supabase.table("profiles") \
# # # # # #             .select("*") \
# # # # # #             .eq("id", user_id) \
# # # # # #             .execute()

# # # # # #         if not profile.data:
# # # # # #             return jsonify({
# # # # # #                 "success": False,
# # # # # #                 "message": "Role not found"
# # # # # #             })

# # # # # #         role = profile.data[0]["role"]

# # # # # #         # Save session (good for security + viva)
# # # # # #         session["user_id"] = user_id
# # # # # #         session["role"] = role

# # # # # #         # Redirect based on role
# # # # # #         if role == "admin":
# # # # # #             redirect_url = "/admin/dashboard"
# # # # # #         elif role in ["coord", "coordinator"]:
# # # # # #             redirect_url = "/coord/dashboard"
# # # # # #         else:
# # # # # #             return jsonify({
# # # # # #                 "success": False,
# # # # # #                 "message": "Invalid role"
# # # # # #             })

# # # # # #         return jsonify({
# # # # # #             "success": True,
# # # # # #             "redirect": redirect_url
# # # # # #         })

# # # # # #     except Exception as e:
# # # # # #         return jsonify({
# # # # # #             "success": False,
# # # # # #             "message": str(e)
# # # # # #         })


# # # # # # # =============================
# # # # # # # LOGOUT
# # # # # # # =============================
# # # # # # @auth_bp.route("/logout")
# # # # # # def logout():
# # # # # #     session.clear()
# # # # # #     return redirect("/login")

# # # # # # final fixed

# # # # # from flask import Blueprint, request, jsonify, render_template, redirect, session
# # # # # from config import supabase

# # # # # auth_bp = Blueprint("auth", __name__)


# # # # # # Login pages
# # # # # @auth_bp.route("/admin/login")
# # # # # def admin_login():
# # # # #     return render_template("admin_login.html")


# # # # # @auth_bp.route("/coord/login")
# # # # # def coord_login():
# # # # #     return render_template("coord_login.html")


# # # # # # =====================
# # # # # # SIMPLE LOGIN API
# # # # # # =====================
# # # # # @auth_bp.route("/api/login", methods=["POST"])
# # # # # def api_login():
# # # # #     data = request.get_json()

# # # # #     email = data.get("email")
# # # # #     password = data.get("password")  # only for demo

# # # # #     # Fetch user from profiles table
# # # # #     user = supabase.table("profiles") \
# # # # #         .select("*") \
# # # # #         .eq("email", email) \
# # # # #         .execute()

# # # # #     if not user.data:
# # # # #         return jsonify({"success": False, "message": "User not found"})

# # # # #     role = user.data[0]["role"]

# # # # #     # Demo password check (for submission)
# # # # #     if password != "12345678":
# # # # #         return jsonify({"success": False, "message": "Wrong password"})

# # # # #     session["role"] = role

# # # # #     if role == "admin":
# # # # #         redirect_url = "/admin/dashboard"
# # # # #     else:
# # # # #         redirect_url = "/coord/dashboard"

# # # # #     return jsonify({"success": True, "redirect": redirect_url})


# # # # # @auth_bp.route("/logout")
# # # # # def logout():
# # # # #     session.clear()
# # # # #     return redirect("/roles")

# # # # from flask import Blueprint, request, jsonify, render_template, session, redirect

# # # # auth_bp = Blueprint("auth", __name__)


# # # # # ==============================
# # # # # LOGIN PAGES
# # # # # ==============================

# # # # @auth_bp.route("/admin/login")
# # # # def admin_login():
# # # #     return render_template("admin_login.html")


# # # # @auth_bp.route("/coord/login")
# # # # def coord_login():
# # # #     return render_template("coord_login.html")


# # # # # ==============================
# # # # # SIMPLE LOGIN API
# # # # # ==============================

# # # # @auth_bp.route("/api/login", methods=["POST"])
# # # # def api_login():
# # # #     try:
# # # #         data = request.get_json()

# # # #         email = data.get("email")
# # # #         password = data.get("password")

# # # #         # DEMO PASSWORD
# # # #         if password != "12345678":
# # # #             return jsonify({
# # # #                 "success": False,
# # # #                 "message": "Invalid password"
# # # #             })

# # # #         # ADMIN LOGIN
# # # #         if email == "admin1@example.com":
# # # #             session["role"] = "admin"
# # # #             return jsonify({
# # # #                 "success": True,
# # # #                 "redirect": "/admin/dashboard"
# # # #             })

# # # #         # COORDINATOR LOGIN
# # # #         elif email == "coord1@example.com":
# # # #             session["role"] = "coord"
# # # #             return jsonify({
# # # #                 "success": True,
# # # #                 "redirect": "/coord/dashboard"
# # # #             })

# # # #         else:
# # # #             return jsonify({
# # # #                 "success": False,
# # # #                 "message": "User not found"
# # # #             })

# # # #     except Exception as e:
# # # #         return jsonify({
# # # #             "success": False,
# # # #             "message": str(e)
# # # #         })


# # # # # ==============================
# # # # # LOGOUT
# # # # # ==============================

# # # # @auth_bp.route("/logout")
# # # # def logout():
# # # #     session.clear()
# # # #     return redirect("/roles")

# # # from flask import Blueprint, request, jsonify
# # # from config import SUPABASE_URL, HEADERS
# # # import requests

# # # auth_bp = Blueprint("auth", __name__)

# # # @auth_bp.route("/api/login", methods=["POST"])
# # # def login():
# # #     data = request.get_json()

# # #     email = data.get("email")
# # #     role = data.get("role")

# # #     url = f"{SUPABASE_URL}/rest/v1/profiles?email=eq.{email}&role=eq.{role}"

# # #     res = requests.get(url, headers=HEADERS)

# # #     if res.status_code == 200 and res.json():
# # #         return jsonify({
# # #             "success": True,
# # #             "redirect": f"/{role}/dashboard"
# # #         })

# # #     return jsonify({
# # #         "success": False,
# # #         "message": "Invalid credentials"
# # #     })


# # correct one
# # from flask import Blueprint, request, jsonify, render_template
# # from config import SUPABASE_URL, HEADERS
# # import requests

# # auth_bp = Blueprint("auth", __name__)

# # # ADMIN LOGIN PAGE
# # @auth_bp.route("/admin/login")
# # def admin_login():
# #     return render_template("admin_login.html")

# # # COORD LOGIN PAGE
# # @auth_bp.route("/coord/login")
# # def coord_login():
# #     return render_template("coord_login.html")


# # # LOGIN API
# # @auth_bp.route("/api/login", methods=["POST"])
# # def login():
# #     data = request.get_json()

# #     email = data.get("email")
# #     role = data.get("role")

# #     # Query Supabase profiles table
# #     url = f"{SUPABASE_URL}/rest/v1/profiles?email=eq.{email}&role=eq.{role}"

# #     res = requests.get(url, headers=HEADERS)

# #     if res.status_code == 200 and res.json():
# #         return jsonify({
# #             "success": True,
# #             "redirect": f"/{role}/dashboard"
# #         })

# #     return jsonify({
# #         "success": False,
# #         "message": "Invalid email or role"
# #     }) 

# #working one
# from flask import Blueprint, render_template, request, redirect, url_for, session
# from config import supabase

# auth_bp = Blueprint("auth", __name__)

# # =========================
# # ADMIN LOGIN PAGE
# # =========================
# @auth_bp.route("/admin/login", methods=["GET", "POST"])
# def admin_login():
#     if request.method == "POST":
#         email = request.form.get("email")
#         password = request.form.get("password")

#         # simple demo password
#         if password != "12345678":
#             return render_template("admin_login.html", error="Wrong password")

#         # check in supabase
#         res = supabase.table("profiles").select("*").eq("email", email).eq("role", "admin").execute()

#         if res.data:
#             session["user"] = email
#             session["role"] = "admin"
#             return redirect("/admin/dashboard")

#         return render_template("admin_login.html", error="Invalid admin")

#     return render_template("admin_login.html")


# # =========================
# # COORD LOGIN PAGE
# # =========================
# @auth_bp.route("/coord/login", methods=["GET", "POST"])
# def coord_login():
#     if request.method == "POST":
#         email = request.form.get("email")
#         password = request.form.get("password")

#         if password != "12345678":
#             return render_template("coord_login.html", error="Wrong password")

#         res = supabase.table("profiles").select("*").eq("email", email).eq("role", "coord").execute()

#         if res.data:
#             session["user"] = email
#             session["role"] = "coord"
#             return redirect("/coord/dashboard")

#         return render_template("coord_login.html", error="Invalid coordinator")

#     return render_template("coord_login.html")


# # =========================
# # LOGOUT
# # =========================
# @auth_bp.route("/logout")
# def logout():
#     session.clear()
#     return redirect("/")

# new
from flask import Blueprint, request, jsonify, session
from config import supabase

auth_bp = Blueprint("auth", __name__)


# ===============================
# SIMPLE LOGIN API (for fetch)
# ===============================
@auth_bp.route("/api/login", methods=["POST"])
def login_api():
    try:
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")
        role = data.get("role")

        # Simple demo password
        if password != "12345678":
            return jsonify({"success": False, "message": "Wrong password"})

        # Check in Supabase table
        res = supabase.table("profiles") \
            .select("*") \
            .eq("email", email) \
            .eq("role", role) \
            .execute()

        if res.data:
            # Save session
            session["user"] = email
            session["role"] = role

            # Redirect based on role
            if role == "admin":
                return jsonify({
                    "success": True,
                    "redirect": "/admin/dashboard"
                })

            if role == "coord":
                return jsonify({
                    "success": True,
                    "redirect": "/coord/dashboard"
                })

        return jsonify({"success": False, "message": "Invalid email or role"})

    except Exception as e:
        return jsonify({"success": False, "message": str(e)})


# ===============================
# LOGOUT
# ===============================
@auth_bp.route("/logout")
def logout():
    session.clear()
    return jsonify({"success": True})