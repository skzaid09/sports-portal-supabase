from flask import Blueprint, render_template, request, jsonify
import os
import requests

player_bp = Blueprint("player", __name__, url_prefix="/player")

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_KEY")

HEADERS = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json",
    "Prefer": "return=representation"
}


# ======================
# PAGES
# ======================

@player_bp.route("/options")
def options():
    return render_template("player/options.html")


@player_bp.route("/register")
def register():
    return render_template("player/register.html")


@player_bp.route("/register/single")
def register_single():
    return render_template("player/register_single.html")


@player_bp.route("/register/team")
def register_team():
    return render_template("player/register_team.html")


# ======================
# SINGLE PLAYER REGISTRATION
# ======================

@player_bp.route("/api/register-single", methods=["POST"])
def api_single():

    try:

        data = request.get_json()

        roll_no = data.get("roll_no")

        # 🔍 CHECK DUPLICATE ROLL NUMBER
        check_res = requests.get(
            f"{SUPABASE_URL}/rest/v1/players?roll_no=eq.{roll_no}&select=roll_no",
            headers=HEADERS
        )

        if check_res.status_code == 200 and len(check_res.json()) > 0:

            return jsonify({
                "success": False,
                "message": "Roll Number already registered"
            })


        # INSERT PLAYER
        payload = {
            "name": data.get("name"),
            "school": data.get("school"),
            "gender": data.get("gender"),
            "roll_no": roll_no,
            "sport": data.get("sport"),
            "type": "single"
        }

        res = requests.post(
            f"{SUPABASE_URL}/rest/v1/players",
            json=payload,
            headers=HEADERS
        )

        if res.status_code in [200, 201]:

            return jsonify({
                "success": True,
                "message": "Player registered successfully"
            })

        else:

            print("Insert error:", res.text)

            return jsonify({
                "success": False,
                "message": "Database error"
            })


    except Exception as e:

        print("Single player error:", e)

        return jsonify({
            "success": False,
            "message": "Server error"
        })


# ======================
# TEAM REGISTRATION
# ======================

@player_bp.route("/api/register-team", methods=["POST"])
def register_team_api():

    try:

        data = request.get_json()

        # ======================
        # CREATE TEAM
        # ======================

        team_payload = {
            "team_name": data["team_name"],
            "school": data["school"],
            "sport": data["sport"]
        }

        team_res = requests.post(
            f"{SUPABASE_URL}/rest/v1/teams",
            json=team_payload,
            headers=HEADERS
        )

        if team_res.status_code not in [200,201]:
            print("Team insert error:", team_res.text)
            return jsonify({
                "success": False,
                "message": "Team creation failed"
            })

        team_data = team_res.json()

        if not team_data:
            return jsonify({
                "success": False,
                "message": "Team not returned from database"
            })

        team_id = team_data[0]["id"]

        # ======================
        # INSERT TEAM PLAYERS
        # ======================

        players = data.get("players", [])

        for p in players:

            player_payload = {
                "team_id": team_id,
                "name": p["name"],
                "roll_no": p["roll_no"]
            }

            res = requests.post(
                f"{SUPABASE_URL}/rest/v1/team_players",
                json=player_payload,
                headers=HEADERS
            )

            if res.status_code not in [200,201]:
                print("Player insert error:", res.text)

        return jsonify({
            "success": True,
            "message": "Team registered successfully"
        })


    except Exception as e:

        print("Team registration error:", e)

        return jsonify({
            "success": False,
            "message": "Server error during team registration"
        })


# ======================
# VIEW EVENTS
# ======================

@player_bp.route("/events")
def player_events():
    return render_template("player/events.html")


@player_bp.route("/api/events")
def api_events():

    res = requests.get(
        f"{SUPABASE_URL}/rest/v1/events?select=*",
        headers=HEADERS
    )

    if res.status_code == 200:
        return jsonify(res.json())
    else:
        return jsonify([])


# ======================
# MATCH SCHEDULE PAGE
# ======================

@player_bp.route("/matches")
def view_matches():
    return render_template("player/matches.html")