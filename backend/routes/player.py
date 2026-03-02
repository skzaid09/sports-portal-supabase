# # #new3
# # from flask import Blueprint, render_template, request, jsonify
# # from flask import Blueprint, render_template

# # player_bp = Blueprint("player", __name__)

# # @player_bp.route("/options")
# # def options():
# #     return render_template("player/options.html")

# # player_bp = Blueprint("player", __name__)

# # @player_bp.route("/register")
# # def register():
# #     return render_template("player/register.html")

# # @player_bp.route("/register/single")
# # def register_single():
# #     return render_template("player/register_single.html")

# # @player_bp.route("/register/team")
# # def register_team():
# #     return render_template("player/register_team.html")


# # # ✅ FIXED SINGLE PLAYER REGISTRATION
# # @player_bp.route("/api/register-single", methods=["POST"])
# # def api_single():
# #     data = request.get_json()

# #     # insert into PROFILES instead of users
# #     user = supabase.table("profiles").insert({
# #         "email": f"{data['roll_no']}@sports.com",
# #         "role": "player"
# #     }).execute()

# #     if not user.data:
# #         return jsonify({"error": "Profile insert failed"})

# #     supabase.table("players").insert({
# #         "name": data["name"],
# #         "department": data["department"],
# #         "roll_no": data["roll_no"],
# #         "sport": data["sport"],
# #         "type": "single",
# #         "user_id": user.data[0]["id"]
# #     }).execute()

# #     return jsonify({"success": True})


# # # TEAM REGISTRATION (UNCHANGED)
# # @player_bp.route("/api/register-team", methods=["POST"])
# # def api_team():
# #     data = request.get_json()

# #     team = supabase.table("teams").insert({
# #         "team_name": data["team_name"],
# #         "department": data["department"],
# #         "sport": data["sport"]
# #     }).execute()

# #     for p in data["players"]:
# #         supabase.table("team_players").insert({
# #             "team_id": team.data[0]["id"],
# #             "name": p["name"],
# #             "roll_no": p["roll_no"]
# #         }).execute()

# #     return jsonify({"success": True})

# # #polish
# from flask import Blueprint, render_template, request, jsonify

# player_bp = Blueprint("player", __name__, url_prefix="/player")


# # ==============================
# # PLAYER PAGES
# # ==============================

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


# # ==============================
# # SINGLE PLAYER REGISTRATION
# # ==============================

# @player_bp.route("/api/register-single", methods=["POST"])
# def api_single():
#     try:
#         data = request.get_json()

#         # ✅ Create profile
#         profile = supabase.table("profiles").insert({
#             "email": f"{data['roll_no']}@sports.com",
#             "role": "player"
#         }).execute()

#         if not profile.data:
#             return jsonify({"success": False, "message": "Profile insert failed"})

#         user_id = profile.data[0]["id"]

#         # ✅ Insert player
#         supabase.table("players").insert({
#             "name": data["name"],
#             "department": data["department"],
#             "roll_no": data["roll_no"],
#             "sport": data["sport"],
#             "type": "single",
#             "user_id": user_id
#         }).execute()

#         return jsonify({"success": True})

#     except Exception as e:
#         print("Single registration error:", e)
#         return jsonify({"success": False, "message": "Server error"})


# # ==============================
# # TEAM REGISTRATION
# # ==============================

# @player_bp.route("/api/register-team", methods=["POST"])
# def api_team():
#     try:
#         data = request.get_json()

#         # ✅ Create team
#         team = supabase.table("teams").insert({
#             "team_name": data["team_name"],
#             "department": data["department"],
#             "sport": data["sport"]
#         }).execute()

#         if not team.data:
#             return jsonify({"success": False, "message": "Team insert failed"})

#         team_id = team.data[0]["id"]

#         # ✅ Insert players
#         for p in data["players"]:
#             supabase.table("team_players").insert({
#                 "team_id": team_id,
#                 "name": p["name"],
#                 "roll_no": p["roll_no"]
#             }).execute()

#         return jsonify({"success": True})

#     except Exception as e:
#         print("Team registration error:", e)
#         return jsonify({"success": False, "message": "Server error"})

from flask import Blueprint, render_template, request, jsonify
import os
import requests

player_bp = Blueprint("player", __name__, url_prefix="/player")

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_SERVICE_KEY")

HEADERS = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json"
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
#polish single player3
import requests
from flask import jsonify, request

@player_bp.route("/api/register-single", methods=["POST"])
def api_single():
    try:
        data = request.get_json()
        print("✅ Received data:", data)

        payload = {
            "name": data["name"],
            "department": data["department"],
            "roll_no": data["roll_no"],
            "sport": data["sport"],
            "type": "single"
        }

        print("📤 Sending to Supabase:", payload)

        res = requests.post(
            f"{SUPABASE_URL}/rest/v1/players",
            json=payload,
            headers=HEADERS
        )

        print("📥 Supabase status:", res.status_code)
        print("📥 Supabase response:", res.text)

        # IMPORTANT
        if res.status_code in [200, 201]:
            return jsonify({"success": True})
        else:
            return jsonify({"success": False, "error": res.text})

    except Exception as e:
        print("❌ ERROR:", e)
        return jsonify({"success": False, "error": str(e)})

# ======================
# TEAM PLAYER
# ======================

@player_bp.route("/api/register-team", methods=["POST"])
def register_team_api():
    try:
        data = request.get_json()

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
            return jsonify({"success": False})

        team = team_res.json()[0]
        team_id = team["id"]

        # insert players
        for p in data["players"]:
            requests.post(
                f"{SUPABASE_URL}/rest/v1/team_players",
                json={
                    "team_id": team_id,
                    "name": p["name"],
                    "roll_no": p["roll_no"]
                },
                headers=HEADERS
            )

        return jsonify({"success": True})

    except Exception as e:
        print("Team error:", e)
        return jsonify({"success": False})