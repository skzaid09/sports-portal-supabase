from flask import Blueprint, render_template, session, redirect, request, jsonify
import requests
import os

admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_ANON_KEY")

HEADERS = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json"
}

# ======================
# LOGIN
# ======================
@admin_bp.route("/login")
def login():
    return render_template("admin/login.html")


# ======================
# DASHBOARD
# ======================
@admin_bp.route("/dashboard")
def dashboard():

    if "user" not in session or session["user"]["role"] != "admin":
        return redirect("/admin/login")

    return render_template("admin/dashboard.html")


# ======================
# GET PLAYERS
# ======================
@admin_bp.route("/api/players")
def get_players():

    res = requests.get(
        f"{SUPABASE_URL}/rest/v1/players?select=*",
        headers=HEADERS
    )

    return jsonify(res.json())


# ======================
# GET TEAMS
# ======================
@admin_bp.route("/api/teams")
def get_teams():

    res = requests.get(
        f"{SUPABASE_URL}/rest/v1/teams?select=*",
        headers=HEADERS
    )

    return jsonify(res.json())


# ======================
# GET EVENTS
# ======================
@admin_bp.route("/api/events")
def get_events():

    res = requests.get(
        f"{SUPABASE_URL}/rest/v1/events?select=*",
        headers=HEADERS
    )

    return jsonify(res.json())


# ======================
# CREATE EVENT
# ======================
@admin_bp.route("/api/create-event", methods=["POST"])
def create_event():

    data = request.get_json()

    payload = {
        "name": data.get("name"),
        "type": data.get("type"),
        "date": data.get("date"),
        "location": data.get("location")
    }

    res = requests.post(
        f"{SUPABASE_URL}/rest/v1/events",
        headers=HEADERS,
        json=payload
    )

    print("SUPABASE RESPONSE:", res.text)

    if res.status_code in [200,201]:
        return jsonify({"success": True})
    else:
        return jsonify({"success": False})

# ======================
# DELETE PLAYER
# ======================
@admin_bp.route("/api/delete-player/<id>", methods=["DELETE"])
def delete_player(id):

    requests.delete(
        f"{SUPABASE_URL}/rest/v1/players?id=eq.{id}",
        headers=HEADERS
    )

    return jsonify({"success": True})


# ======================
# DELETE TEAM
# ======================
@admin_bp.route("/api/delete-team/<id>", methods=["DELETE"])
def delete_team(id):

    requests.delete(
        f"{SUPABASE_URL}/rest/v1/teams?id=eq.{id}",
        headers=HEADERS
    )

    return jsonify({"success": True})


# ======================
# DELETE EVENT
# ======================
@admin_bp.route("/api/delete-event/<id>", methods=["DELETE"])
def delete_event(id):

    requests.delete(
        f"{SUPABASE_URL}/rest/v1/events?id=eq.{id}",
        headers=HEADERS
    )

    return jsonify({"success": True})