from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import psycopg2
import os

app = Flask(__name__)
app.secret_key = "super_secret_key_123"

# =========================
# DATABASE CONFIG (Supabase)
# =========================
DATABASE_URL = os.environ.get(
    "DATABASE_URL",
    "postgresql://postgres:YOUR_PASSWORD@db.xxxxx.supabase.co:5432/postgres"
)

def get_db():
    return psycopg2.connect(DATABASE_URL)

# =========================
# HOME + ROLES
# =========================
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/roles")
def roles():
    return render_template("roles.html")

# =========================
# ADMIN
# =========================
@app.route("/admin/login", methods=["GET", "POST"])
def admin_login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # Demo static login
        if username == "admin" and password == "admin123":
            session["role"] = "admin"
            return redirect("/admin/dashboard")
        return "Invalid Admin Credentials"

    return render_template("admin/login.html")

@app.route("/admin/dashboard")
def admin_dashboard():
    if session.get("role") != "admin":
        return redirect("/admin/login")
    return render_template("admin/dashboard.html")

# =========================
# COORDINATOR
# =========================
@app.route("/coord/login", methods=["GET", "POST"])
def coord_login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == "coord" and password == "coord123":
            session["role"] = "coord"
            return redirect("/coord/dashboard")
        return "Invalid Coordinator Credentials"

    return render_template("coord/login.html")

@app.route("/coord/dashboard")
def coord_dashboard():
    if session.get("role") != "coord":
        return redirect("/coord/login")
    return render_template("coord/dashboard.html")

# =========================
# PLAYER
# =========================
@app.route("/player/dashboard")
def player_dashboard():
    return render_template("player/dashboard.html")

@app.route("/player/register")
def player_register():
    return render_template("player/register.html")

@app.route("/player/register/single")
def register_single():
    return render_template("player/register_single.html")

@app.route("/player/register/team")
def register_team():
    return render_template("player/register_team.html")

# =========================
# API: REGISTER SINGLE PLAYER
# =========================
@app.route("/player/api/register-single", methods=["POST"])
def api_register_single():
    data = request.json
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO players (name, department, roll_no, sport)
            VALUES (%s, %s, %s, %s)
        """, (data["name"], data["department"], data["roll_no"], data["sport"]))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({"success": True})
    except Exception as e:
        print("ERROR:", e)
        return jsonify({"error": str(e)}), 500

# =========================
# API: REGISTER TEAM
# =========================
@app.route("/player/api/register-team", methods=["POST"])
def api_register_team():
    data = request.json
    try:
        conn = get_db()
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO teams (team_name, department, sport)
            VALUES (%s, %s, %s)
            RETURNING id
        """, (data["team_name"], data["department"], data["sport"]))

        team_id = cur.fetchone()[0]

        for p in data["players"]:
            cur.execute("""
                INSERT INTO team_players (team_id, name, roll_no)
                VALUES (%s, %s, %s)
            """, (team_id, p["name"], p["roll_no"]))

        conn.commit()
        cur.close()
        conn.close()
        return jsonify({"success": True})
    except Exception as e:
        print("ERROR:", e)
        return jsonify({"error": str(e)}), 500

# =========================
# LOGOUT
# =========================
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

# =========================
# PORT FIX FOR RENDER
# =========================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
