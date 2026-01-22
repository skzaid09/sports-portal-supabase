from flask import Flask, render_template, request, jsonify
from supabase_client import supabase

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/roles")
def roles():
    return render_template("roles.html")

@app.route("/health")
def health():
    return "OK"

# Admin
@app.route("/admin/login")
def admin_login():
    return render_template("admin/login.html")

@app.route("/admin/dashboard")
def admin_dashboard():
    users = supabase.table("users").select("*").execute().data
    return render_template("admin/dashboard.html", users=users)

# Coordinator
@app.route("/coord/login")
def coord_login():
    return render_template("coord/login.html")

@app.route("/coord/dashboard")
def coord_dashboard():
    matches = supabase.table("matches").select("*").execute().data
    return render_template("coord/dashboard.html", matches=matches)

# Player
@app.route("/player/register")
def player_register():
    return render_template("player/register.html")

@app.route("/player/register/single")
def player_single():
    return render_template("player/register_single.html")

@app.route("/player/register/team")
def player_team():
    return render_template("player/register_team.html")

@app.route("/player/api/register-single", methods=["POST"])
def register_single():
    supabase.table("players").insert(request.json).execute()
    return jsonify(success=True)

@app.route("/player/api/register-team", methods=["POST"])
def register_team():
    data = request.json
    team = supabase.table("teams").insert({
        "team_name": data["team_name"],
        "department": data["department"],
        "sport": data["sport"]
    }).execute().data[0]

    for p in data["players"]:
        supabase.table("team_players").insert({
            "team_id": team["id"],
            "name": p["name"],
            "roll_no": p["roll_no"]
        }).execute()

    return jsonify(success=True)

if __name__ == "__main__":
    app.run()
