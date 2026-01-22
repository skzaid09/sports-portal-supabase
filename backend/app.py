from flask import Flask, render_template, request, redirect, url_for, session
from supabase import create_client, Client
import os

app = Flask(__name__)
app.secret_key = "supersecretkey123"

# Supabase config
SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

# -------------------- HOME --------------------
@app.route("/")
def index():
    return render_template("index.html")

# -------------------- ROLES --------------------
@app.route("/roles")
def roles():
    return render_template("roles.html")

# -------------------- ADMIN --------------------
@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        if request.form["username"] == "admin" and request.form["password"] == "admin123":
            session["admin"] = True
            return redirect("/admin/dashboard")
    return render_template("admin/login.html")

@app.route("/admin/dashboard")
def admin_dashboard():
    if not session.get("admin"):
        return redirect("/admin/login")
    return render_template("admin/dashboard.html")

# -------------------- COORDINATOR --------------------
@app.route("/coord/login", methods=["GET", "POST"])
def coord_login():
    if request.method == "POST":
        if request.form["username"] == "coord" and request.form["password"] == "coord123":
            session["coord"] = True
            return redirect("/coord/dashboard")
    return render_template("coord/login.html")

@app.route("/coord/dashboard")
def coord_dashboard():
    if not session.get("coord"):
        return redirect("/coord/login")
    return render_template("coord/dashboard.html")

# -------------------- PLAYER --------------------
@app.route("/player/register")
def player_register():
    return render_template("player/register.html")

@app.route("/player/register/single", methods=["GET", "POST"])
def register_single():
    if request.method == "POST":
        data = {
            "name": request.form["name"],
            "department": request.form["department"],
            "roll_no": request.form["roll_no"],
            "sport": request.form["sport"]
        }
        supabase.table("players").insert(data).execute()
        return redirect("/")
    return render_template("player/register_single.html")

@app.route("/player/register/team", methods=["GET", "POST"])
def register_team():
    if request.method == "POST":
        data = {
            "team_name": request.form["team_name"],
            "department": request.form["department"],
            "sport": request.form["sport"]
        }
        supabase.table("teams").insert(data).execute()
        return redirect("/")
    return render_template("player/register_team.html")

# -------------------- LOGOUT --------------------
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

# -------------------- RUN --------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
