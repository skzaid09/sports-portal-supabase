from flask import Blueprint, render_template
from config import supabase

admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/login")
def login():
    return render_template("admin/login.html")

@admin_bp.route("/dashboard")
def dashboard():
    users = supabase.table("users").select("*").execute().data
    return render_template("admin/dashboard.html", users=users)

@admin_bp.route('/logout')
def logout():
    session.clear()
    return redirect('/')
