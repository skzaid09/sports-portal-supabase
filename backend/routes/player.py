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
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Team Registration</title>

<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">

<style>
body{
  background: linear-gradient(135deg,#fc466b,#3f5efb);
  min-height:100vh;
}
.navbar{
  background: linear-gradient(to right,#000428,#004e92);
}
.card{
  border-radius:20px;
  background:rgba(150,178,179,0.95);
}
.btn-success{
  border-radius:30px;
}
</style>
</head>

<body>

<nav class="navbar navbar-dark shadow">
<div class="container">
<span class="navbar-brand fw-bold">🤝 Team Registration</span>
<a href="/" class="btn btn-outline-light btn-sm">Logout</a>
</div>
</nav>

<div class="container py-5">
<div class="row justify-content-center">
<div class="col-lg-7">

<div class="card shadow-lg p-4">

<h3 class="text-center mb-4">Register Team</h3>

<form id="teamForm">

<input type="text" class="form-control mb-3" id="team_name" placeholder="Team Name" required>

<input type="text" class="form-control mb-3" id="department" placeholder="Department" required>

<select class="form-select mb-3" id="sport" required>
<option value="">Select Sport</option>
</select>

<h5 class="mt-3">Team Members</h5>

<div id="players-container">

<div class="row g-2 mb-2">
<div class="col-md-6">
<input class="form-control" placeholder="Player Name" required>
</div>
<div class="col-md-6">
<input class="form-control" placeholder="Roll No" required>
</div>
</div>

</div>

<button type="button" class="btn btn-outline-primary mb-3" onclick="addPlayer()">+ Add Player</button>

<div id="loader" class="text-center mb-3" style="display:none;">
<div class="spinner-border text-primary"></div>
<p>Registering team...</p>
</div>

<button type="submit" class="btn btn-success w-100">Register Team</button>

</form>

<a href="/player/register" class="btn btn-link mt-3">← Back to Options</a>

</div>
</div>
</div>
</div>

<!-- TOAST -->

<div class="position-fixed bottom-0 end-0 p-3">
<div id="liveToast" class="toast text-bg-success border-0">
<div class="d-flex">
<div class="toast-body" id="toastMessage"></div>
<button class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast"></button>
</div>
</div>
</div>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js"></script>

<script>

function showToast(message,type="success"){
const toastEl=document.getElementById("liveToast")
toastEl.className="toast text-bg-"+type+" border-0"
document.getElementById("toastMessage").innerText=message
new bootstrap.Toast(toastEl).show()
}

function addPlayer(){
const container=document.getElementById("players-container")

const row=document.createElement("div")
row.className="row g-2 mb-2"

row.innerHTML=`
<div class="col-md-6">
<input class="form-control" placeholder="Player Name" required>
</div>
<div class="col-md-6">
<input class="form-control" placeholder="Roll No" required>
</div>
`

container.appendChild(row)
}

async function loadTeamEvents(){

const res=await fetch("/coord/api/events")
const events=await res.json()

let options="<option value=''>Select Sport</option>"

events.forEach(e=>{
if(e.type && e.type.toLowerCase()=="team"){
options+=`<option value="${e.name}">${e.name}</option>`
}
})

document.getElementById("sport").innerHTML=options
}

loadTeamEvents()


document.getElementById("teamForm").addEventListener("submit",async function(e){

e.preventDefault()

const loader=document.getElementById("loader")

const players=[]

document.querySelectorAll("#players-container .row").forEach(row=>{
const inputs=row.querySelectorAll("input")

players.push({
name:inputs[0].value,
roll_no:inputs[1].value
})
})

const data={
team_name:document.getElementById("team_name").value,
department:document.getElementById("department").value,
sport:document.getElementById("sport").value,
players:players
}

loader.style.display="block"

try{

const res=await fetch("/player/api/register-team",{
method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify(data)
})

loader.style.display="none"

const result=await res.json()

if(result.success){

showToast("🎉 Team Registered Successfully!")

setTimeout(()=>{
window.location.href="/roles"
},1500)

}else{

showToast("Registration Failed","danger")

}

}catch(err){

loader.style.display="none"

showToast("Server Error","danger")

}

})

</script>

</body>
</html>