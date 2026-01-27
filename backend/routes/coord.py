from flask import Blueprint, render_template, session, redirect
from config import supabase

coord_bp = Blueprint("coord", __name__)

@coord_bp.route("/login")
def login():
    return render_template("coord/login.html")

@coord_bp.route("/dashboard")
def dashboard():
    if "user" not in session or session["user"]["role"] != "coord":
        return redirect("/")

    try:
        response = supabase.table("matches").select("*").execute()
        matches = response.data if response.data else []
    except Exception as e:
        print("❌ Supabase error in coord dashboard:", e)
        matches = []   # fail safely

    return render_template("coord/dashboard.html", matches=matches)
