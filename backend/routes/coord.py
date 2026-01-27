# coord.py
from flask import Blueprint, render_template, session, redirect
from config import supabase

coord_bp = Blueprint("coord", __name__, url_prefix="/coord")

@coord_bp.route("/login")
def login():
    return render_template("coord/login.html")

@coord_bp.route("/dashboard")
def dashboard():
    if "user" not in session or session["user"]["role"] != "coord":
        return redirect("/coord/login")

    try:
        matches = supabase.table("matches").select("*").execute().data
    except Exception:
        matches = []

    return render_template("coord/dashboard.html", matches=matches)
