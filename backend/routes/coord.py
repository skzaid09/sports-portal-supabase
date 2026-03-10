from flask import Blueprint, render_template, session, redirect, request, jsonify
import requests
import os

coord_bp = Blueprint("coord", __name__, url_prefix="/coord")

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_ANON_KEY")

HEADERS = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json"
}


# ======================
# LOGIN PAGE
# ======================
@coord_bp.route("/login")
def login():
    return render_template("coord/login.html")


# ======================
# DASHBOARD PAGE
# ======================
@coord_bp.route("/dashboard")
def dashboard():
    if "user" not in session or session["user"]["role"] != "coord":
        return redirect("/coord/login")

    return render_template("coord/dashboard.html")


# ======================
# SAVE MATCH
# ======================
@coord_bp.route("/api/schedule-match", methods=["POST"])
def schedule_match():
    try:
        data = request.get_json()

        payload = {
            "event": data.get("event"),
            "team1": data.get("team1"),
            "team2": data.get("team2"),
            "date": data.get("date"),
            "status": "Scheduled"
        }

        res = requests.post(
            f"{SUPABASE_URL}/rest/v1/matches",
            headers=HEADERS,
            json=payload
        )

        if res.status_code in [200, 201]:
            return jsonify({"success": True})
        else:
            print("MATCH SAVE ERROR:", res.text)
            return jsonify({"success": False})

    except Exception as e:
        print("ERROR:", e)
        return jsonify({"success": False})


# ======================
# FETCH MATCHES
# ======================
@coord_bp.route("/api/get-matches")
def get_matches():
    try:
        res = requests.get(
            f"{SUPABASE_URL}/rest/v1/matches?select=*",
            headers=HEADERS
        )

        if res.status_code == 200:
            return jsonify(res.json())
        else:
            return jsonify([])

    except Exception as e:
        print("FETCH ERROR:", e)
        return jsonify([])


# ======================
# FETCH EVENTS
# ======================
@coord_bp.route("/api/events")
def get_events():
    try:
        res = requests.get(
            f"{SUPABASE_URL}/rest/v1/events?select=*",
            headers=HEADERS
        )

        if res.status_code == 200:
            return jsonify(res.json())
        else:
            return jsonify([])

    except Exception as e:
        print("EVENT FETCH ERROR:", e)
        return jsonify([])


# ======================
# FETCH TEAMS
# ======================
@coord_bp.route("/api/teams")
def get_teams():
    try:
        res = requests.get(
            f"{SUPABASE_URL}/rest/v1/teams?select=*",
            headers=HEADERS
        )

        if res.status_code == 200:
            return jsonify(res.json())
        else:
            return jsonify([])

    except Exception as e:
        print("TEAM FETCH ERROR:", e)
        return jsonify([])

# ======================
# AUTO GENERATE MATCHES
# ======================
@coord_bp.route("/api/generate-matches", methods=["POST"])
def generate_matches():
    try:
        data = request.get_json()
        event_name = data.get("event")

        # fetch teams from Supabase
        team_res = requests.get(
            f"{SUPABASE_URL}/rest/v1/teams?select=*",
            headers=HEADERS
        )

        if team_res.status_code != 200:
            return jsonify({"success": False})

        teams = team_res.json()

        if len(teams) < 2:
            return jsonify({"success": False, "message": "Not enough teams"})

        matches_created = []

        # pair teams automatically
        for i in range(0, len(teams), 2):

            if i+1 >= len(teams):
                break

            team1 = teams[i]["team_name"]
            team2 = teams[i+1]["team_name"]

            payload = {
                "event": event_name,
                "team1": team1,
                "team2": team2,
                "date": None,
                "status": "Scheduled"
            }

            res = requests.post(
                f"{SUPABASE_URL}/rest/v1/matches",
                headers=HEADERS,
                json=payload
            )

            if res.status_code in [200, 201]:
                matches_created.append(f"{team1} vs {team2}")

        return jsonify({
            "success": True,
            "matches": matches_created
        })

    except Exception as e:
        print("GENERATOR ERROR:", e)
        return jsonify({"success": False})