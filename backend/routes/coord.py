from flask import Blueprint, render_template, session, redirect

coord_bp = Blueprint("coord", __name__)

@coord_bp.route("/dashboard")
def dashboard():
    if "user" not in session or session["user"]["role"] != "coord":
        return redirect("/")
    return render_template("coord/dashboard.html")
