from flask import Blueprint, render_template, request, redirect, session
from supabase import create_client
import os

auth_bp = Blueprint("auth", __name__)

supabase = create_client(
    os.environ.get("SUPABASE_URL"),
    os.environ.get("SUPABASE_ANON_KEY")
)

# ---------- ADMIN LOGIN ----------
@auth_bp.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    error = None

    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        try:
            auth = supabase.auth.sign_in_with_password({
                "email": email,
                "password": password
            })

            user = auth.user
            profile = supabase.table("profiles") \
                .select("role") \
                .eq("id", user.id) \
                .single() \
                .execute()

            if profile.data["role"] != "admin":
                error = "Not an admin account"
            else:
                session["user_id"] = user.id
                session["role"] = "admin"
                return redirect("/admin/dashboard")

        except Exception as e:
            error = str(e)

    return render_template("admin/login.html", error=error)


# ---------- COORD LOGIN ----------
@auth_bp.route("/coord/login", methods=["GET", "POST"])
def coord_login():
    error = None

    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        try:
            auth = supabase.auth.sign_in_with_password({
                "email": email,
                "password": password
            })

            user = auth.user
            profile = supabase.table("profiles") \
                .select("role") \
                .eq("id", user.id) \
                .single() \
                .execute()

            if profile.data["role"] != "coord":
                error = "Not a coordinator account"
            else:
                session["user_id"] = user.id
                session["role"] = "coord"
                return redirect("/coord/dashboard")

        except Exception as e:
            error = str(e)

    return render_template("coord/login.html", error=error)
