from flask import Blueprint, render_template, session, redirect
from config import supabase

admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/dashboard")
def dashboard():
    if "user" not in session or session["user"]["role"] != "admin":
        return redirect("/")
    users = supabase.table("users").select("*").execute().data
    return render_template("admin/login.html", users=users)
