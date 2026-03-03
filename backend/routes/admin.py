# # # # # # #new3
# # # # # # from flask import Blueprint, render_template, session, redirect

# # # # # # admin_bp = Blueprint("admin", __name__, url_prefix="/admin")


# # # # # # @admin_bp.route("/login")
# # # # # # def login():
# # # # # #     return render_template("admin/login.html")


# # # # # # @admin_bp.route("/dashboard")
# # # # # # def dashboard():
# # # # # #     if "role" not in session or session["role"] != "admin":
# # # # # #         return redirect("/admin/login")

# # # # # #     return render_template("admin/dashboard.html")

# # # # # #new4
# # # # # from flask import Blueprint, render_template, session, redirect

# # # # # admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

# # # # # @admin_bp.route("/login")
# # # # # def login():
# # # # #     return render_template("admin/login.html")

# # # # # @admin_bp.route("/dashboard")
# # # # # def dashboard():
# # # # #     if "user" not in session or session["user"]["role"] != "admin":
# # # # #         return redirect("/admin/login")
# # # # #     return render_template("admin/dashboard.html")

# # # # #polish
# # # from flask import Blueprint, render_template, session, redirect

# # # admin_bp = Blueprint("admin", __name__, url_prefix="/admin")


# # # # ADMIN LOGIN
# # # @admin_bp.route("/login")
# # # def login():
# # #     return render_template("admin/login.html")


# # # # ADMIN DASHBOARD
# # # @admin_bp.route("/dashboard")
# # # def dashboard():
# # #     if "user" not in session or session["user"]["role"] != "admin":
# # #         return redirect("/admin/login")

# # #     return render_template("admin/dashboard.html")

# # #dont know
# # from flask import Blueprint, render_template, session, redirect
# # import requests
# # import os

# # admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

# # SUPABASE_URL = os.getenv("SUPABASE_URL")
# # SUPABASE_KEY = os.getenv("SUPABASE_ANON_KEY")

# # HEADERS = {
# #     "apikey": SUPABASE_KEY,
# #     "Authorization": f"Bearer {SUPABASE_KEY}"
# # }

# # # LOGIN
# # @admin_bp.route("/login")
# # def login():
# #     return render_template("admin/login.html")


# # # DASHBOARD
# # @admin_bp.route("/dashboard")
# # def dashboard():
# #     if "user" not in session or session["user"]["role"] != "admin":
# #         return redirect("/admin/login")

# #     # 🔥 fetch players
# #     players = requests.get(
# #         f"{SUPABASE_URL}/rest/v1/players?select=*",
# #         headers=HEADERS
# #     ).json()

# #     # 🔥 fetch teams
# #     teams = requests.get(
# #         f"{SUPABASE_URL}/rest/v1/teams?select=*",
# #         headers=HEADERS
# #     ).json()

# #     return render_template(
# #         "admin/dashboard.html",
# #         players=players,
# #         teams=teams
# #     )

# #admin polish

# from flask import Blueprint, render_template, session, redirect, request, jsonify
# import requests
# import os

# admin_bp = Blueprint("admin", __name__, url_prefix="/admin")

# SUPABASE_URL = os.getenv("SUPABASE_URL")
# SUPABASE_KEY = os.getenv("SUPABASE_ANON_KEY")

# HEADERS = {
#     "apikey": SUPABASE_KEY,
#     "Authorization": f"Bearer {SUPABASE_KEY}",
#     "Content-Type": "application/json"
# }


# # ======================
# # LOGIN
# # ======================
# @admin_bp.route("/login")
# def login():
#     return render_template("admin/login.html")


# # ======================
# # DASHBOARD
# # ======================
# @admin_bp.route("/dashboard")
# def dashboard():
#     if "user" not in session or session["user"]["role"] != "admin":
#         return redirect("/admin/login")

#     return render_template("admin/dashboard.html")


# # ======================
# # GET PLAYERS
# # ======================
# @admin_bp.route("/api/players")
# def get_players():
#     res = requests.get(
#         f"{SUPABASE_URL}/rest/v1/players?select=*",
#         headers=HEADERS
#     )
#     return jsonify(res.json())


# # ======================
# # GET TEAMS
# # ======================
# @admin_bp.route("/api/teams")
# def get_teams():
#     res = requests.get(
#         f"{SUPABASE_URL}/rest/v1/teams?select=*",
#         headers=HEADERS
#     )
#     return jsonify(res.json())


# # ======================
# # DELETE PLAYER
# # ======================
# @admin_bp.route("/api/delete-player/<player_id>", methods=["DELETE"])
# def delete_player(player_id):
#     res = requests.delete(
#         f"{SUPABASE_URL}/rest/v1/players?id=eq.{player_id}",
#         headers=HEADERS
#     )
#     return jsonify({"success": res.status_code in [200,204]})


# # ======================
# # DELETE TEAM
# # ======================
# @admin_bp.route("/api/delete-team/<team_id>", methods=["DELETE"])
# def delete_team(team_id):
#     res = requests.delete(
#         f"{SUPABASE_URL}/rest/v1/teams?id=eq.{team_id}",
#         headers=HEADERS
#     )
#     return jsonify({"success": res.status_code in [200,204]})


#     admin polish2

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
    res = requests.get(f"{SUPABASE_URL}/rest/v1/players?select=*", headers=HEADERS)
    return jsonify(res.json())


# ======================
# GET TEAMS
# ======================
@admin_bp.route("/api/teams")
def get_teams():
    res = requests.get(f"{SUPABASE_URL}/rest/v1/teams?select=*", headers=HEADERS)
    return jsonify(res.json())


# ======================
# GET EVENTS
# ======================
@admin_bp.route("/api/events")
def get_events():
    res = requests.get(f"{SUPABASE_URL}/rest/v1/events?select=*", headers=HEADERS)
    return jsonify(res.json())


# ======================
# CREATE EVENT
# ======================
@admin_bp.route("/api/create-event", methods=["POST"])
def create_event():
    data = request.get_json()

    payload = {
        "name": data.get("name"),
        "date": data.get("date"),
        "location": data.get("location")
    }

    res = requests.post(
        f"{SUPABASE_URL}/rest/v1/events",
        headers=HEADERS,
        json=payload
    )

    return jsonify({"success": res.status_code in [200,201]})


# ======================
# DELETE PLAYER
# ======================
@admin_bp.route("/api/delete-player/<id>", methods=["DELETE"])
def delete_player(id):
    res = requests.delete(
        f"{SUPABASE_URL}/rest/v1/players?id=eq.{id}",
        headers=HEADERS
    )
    return jsonify({"success": True})


# ======================
# DELETE TEAM
# ======================
@admin_bp.route("/api/delete-team/<id>", methods=["DELETE"])
def delete_team(id):
    res = requests.delete(
        f"{SUPABASE_URL}/rest/v1/teams?id=eq.{id}",
        headers=HEADERS
    )
    return jsonify({"success": True})


# ======================
# DELETE EVENT
# ======================
@admin_bp.route("/api/delete-event/<id>", methods=["DELETE"])
def delete_event(id):
    res = requests.delete(
        f"{SUPABASE_URL}/rest/v1/events?id=eq.{id}",
        headers=HEADERS
    )
    return jsonify({"success": True})