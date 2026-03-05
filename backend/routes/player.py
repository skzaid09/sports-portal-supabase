# # correct one
# from flask import Blueprint, render_template, request, jsonify
# import os
# import requests

# player_bp = Blueprint("player", __name__, url_prefix="/player")

# SUPABASE_URL = os.getenv("SUPABASE_URL")
# SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_KEY")

# HEADERS = {
#     "apikey": SUPABASE_KEY,
#     "Authorization": f"Bearer {SUPABASE_KEY}",
#     "Content-Type": "application/json"
# }


# # ======================
# # PAGES
# # ======================

# @player_bp.route("/options")
# def options():
#     return render_template("player/options.html")


# @player_bp.route("/register")
# def register():
#     return render_template("player/register.html")


# @player_bp.route("/register/single")
# def register_single():
#     return render_template("player/register_single.html")


# @player_bp.route("/register/team")
# def register_team():
#     return render_template("player/register_team.html")


# # ======================
# # SINGLE PLAYER
# # ======================
# #polish single player3
# import requests
# from flask import jsonify, request

# @player_bp.route("/api/register-single", methods=["POST"])
# def api_single():
#     try:
#         data = request.get_json()
#         print("✅ Received data:", data)

#         payload = {
#             "name": data["name"],
#             "department": data["department"],
#             "roll_no": data["roll_no"],
#             "sport": data["sport"],
#             "type": "single"
#         }

#         print("📤 Sending to Supabase:", payload)

#         res = requests.post(
#             f"{SUPABASE_URL}/rest/v1/players",
#             json=payload,
#             headers=HEADERS
#         )

#         print("📥 Supabase status:", res.status_code)
#         print("📥 Supabase response:", res.text)

#         # IMPORTANT
#         if res.status_code in [200, 201]:
#             return jsonify({"success": True})
#         else:
#             return jsonify({"success": False, "error": res.text})

#     except Exception as e:
#         print("❌ ERROR:", e)
#         return jsonify({"success": False, "error": str(e)})

# # ======================
# # TEAM PLAYER
# # ======================

# @player_bp.route("/api/register-team", methods=["POST"])
# def register_team_api():
#     try:
#         data = request.get_json()

#         team_payload = {
#             "team_name": data["team_name"],
#             "department": data["department"],
#             "sport": data["sport"]
#         }

#         team_res = requests.post(
#             f"{SUPABASE_URL}/rest/v1/teams",
#             json=team_payload,
#             headers=HEADERS
#         )

#         if team_res.status_code not in [200, 201]:
#             return jsonify({"success": False})

#         team = team_res.json()[0]
#         team_id = team["id"]

#         # insert players
#         for p in data["players"]:
#             requests.post(
#                 f"{SUPABASE_URL}/rest/v1/team_players",
#                 json={
#                     "team_id": team_id,
#                     "name": p["name"],
#                     "roll_no": p["roll_no"]
#                 },
#                 headers=HEADERS
#             )

#         return jsonify({"success": True})

#     except Exception as e:
#         print("Team error:", e)
#         return jsonify({"success": False})

#         above is correct

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
# SINGLE PLAYER
# ======================

@player_bp.route("/api/register-single", methods=["POST"])
def api_single():
    try:
        data = request.get_json()

        payload = {
            "name": data["name"],
            "department": data["department"],
            "roll_no": data["roll_no"],
            "sport": data["sport"],
            "type": "single"
        }

        res = requests.post(
            f"{SUPABASE_URL}/rest/v1/players",
            json=payload,
            headers=HEADERS
        )

        if res.status_code in [200, 201]:
            return jsonify({"success": True})
        else:
            return jsonify({"success": False, "error": res.text})

    except Exception as e:
        print("Single player error:", e)
        return jsonify({"success": False})


# ======================
# TEAM REGISTRATION
# ======================

@player_bp.route("/api/register-team", methods=["POST"])
def register_team_api():
    try:
        data = request.get_json()

        # create team
        team_payload = {
            "team_name": data["team_name"],
            "department": data["department"],
            "sport": data["sport"]
        }

        team_res = requests.post(
            f"{SUPABASE_URL}/rest/v1/teams",
            json=team_payload,
            headers=HEADERS
        )

        if team_res.status_code not in [200, 201]:
            print("Team insert error:", team_res.text)
            return jsonify({"success": False})

        team_data = team_res.json()

        if not team_data:
            return jsonify({"success": False})

        team_id = team_data[0]["id"]

        # insert players
        for p in data["players"]:

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

            if res.status_code not in [200, 201]:
                print("Player insert error:", res.text)

        return jsonify({"success": True})

    except Exception as e:
        print("Team error:", e)
        return jsonify({"success": False})


# Events

# show events page
@player_bp.route("/events")
def player_events():
    return render_template("player/events.html")


# fetch events API
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