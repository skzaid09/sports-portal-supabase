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

    # delete players of the team first
    requests.delete(
        f"{SUPABASE_URL}/rest/v1/team_players?team_id=eq.{id}",
        headers=HEADERS
    )

    # delete team
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

# ======================
# EVENT ANALYTICS
# ======================
@admin_bp.route("/api/event-analytics")
def event_analytics():

    # events
    events = requests.get(
        f"{SUPABASE_URL}/rest/v1/events?select=*",
        headers=HEADERS
    ).json()

    # individual players
    players = requests.get(
        f"{SUPABASE_URL}/rest/v1/players?select=*",
        headers=HEADERS
    ).json()

    # teams
    teams = requests.get(
        f"{SUPABASE_URL}/rest/v1/teams?select=*",
        headers=HEADERS
    ).json()

    # team players
    team_players = requests.get(
        f"{SUPABASE_URL}/rest/v1/team_players?select=*",
        headers=HEADERS
    ).json()

    result = []

    for event in events:

        event_players = []

        # individual players
        for p in players:
            if p.get("sport","").lower() == event["name"].lower():

                event_players.append({
                    "id": p["id"],
                    "name": p["name"],
                    "roll_no": p["roll_no"],
                    "school": p["school"],
                    "team_name": "Individual"
                })

        # team players
        for tp in team_players:

            team = next((t for t in teams if t["id"] == tp["team_id"]), None)

            if team and team["sport"].lower() == event["name"].lower():

                event_players.append({
                    "id": tp["id"],
                    "name": tp["name"],
                    "roll_no": tp["roll_no"],
                    "school": team["school"],
                    "team_name": team["team_name"]
                })

        result.append({
            "event": event["name"],
            "type": event["type"],
            "date": event["date"],
            "players": event_players
        })

    return jsonify(result)