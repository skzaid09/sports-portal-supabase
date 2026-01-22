from flask import Flask, render_template, request, jsonify, redirect, url_for
from supabase import create_client
import os

# ---------------- CONFIG ----------------

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

app = Flask(__name__, template_folder="../templates", static_folder="../static")

# ---------------- ROUTES ----------------

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/roles")
def roles():
    return render_template("roles.html")

# ---------------- ADMIN ----------------

@app.route("/admin/login")
def admin_login():
    return render_template("admin/login.html")

@app.route("/admin/dashboard")
def admin_dashboard():
    return render_template("admin/dashboard.html")

# ---------------- COORDINATOR ----------------

@app.route("/coord/login")
def coord_login():
    return render_template("coord/login.html")

@app.route("/coord/dashboard")
def coord_dashboard():
    return render_template("coord/dashboard.html")

# ---------------- PLAYER ----------------

@app.route("/player/register")
def player_register():
    return render_template("player/register.html")

@app.route("/player/register/single")
def player_register_single():
    return render_template("player/register_single.html")

@app.route("/player/register/team")
def player_register_team():
    return render_template("player/register_team.html")

# ---------------- API: REGISTER SINGLE PLAYER ----------------

@app.route("/player/api/register-single", methods=["POST"])
def register_single():
    data = request.json
    try:
        supabase.table("players").insert({
            "name": data["name"],
            "department": data["department"],
            "roll_no": data["roll_no"],
            "sport": data["sport"]
        }).execute()
        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

# ---------------- API: REGISTER TEAM ----------------

@app.route("/player/api/register-team", methods=["POST"])
def register_team():
    data = request.json
    try:
        team = supabase.table("teams").insert({
            "team_name": data["team_name"],
            "department": data["department"],
            "sport": data["sport"]
        }).execute()

        team_id = team.data[0]["id"]

        for player in data["players"]:
            supabase.table("team_players").insert({
                "team_id": team_id,
                "name": player["name"],
                "roll_no": player["roll_no"]
            }).execute()

        return jsonify({"success": True})
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

# ---------------- LOGIN API ----------------

@app.route("/api/login", methods=["POST"])
def login():
    data = request.json
    role = data.get("role")

    if role == "admin":
        return jsonify({"success": True, "redirect": "/admin/dashboard"})
    elif role == "coord":
        return jsonify({"success": True, "redirect": "/coord/dashboard"})
    elif role == "player":
        return jsonify({"success": True, "redirect": "/player/register"})
    else:
        return jsonify({"success": False, "message": "Invalid role"}), 400

# ---------------- RUN ----------------

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
