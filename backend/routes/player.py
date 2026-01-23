# backend/routes/player.py
from flask import Blueprint, render_template, request, jsonify
from config import supabase
from datetime import datetime

player_bp = Blueprint('player', __name__)

@player_bp.route('/register')
def register():
    return render_template('player/register.html')

@player_bp.route('/register/single')
def register_single():
    return render_template('player/register_single.html')

@player_bp.route('/register/team')
def register_team():
    return render_template('player/register_team.html')

@player_bp.route('/api/register-single', methods=['POST'])
def register_single_api():
    data = request.get_json()
    
    # Create auth user
    try:
        auth_response = supabase.auth.sign_up({
            "email": f"{data['roll_no']}@sports.local",
            "password": "default123"
        })
        
        # Create profile
        supabase.table('users').insert({
            "email": f"{data['roll_no']}@sports.local",
            "role": "player"
        }).execute()
        
        # Insert player data
        supabase.table('players').insert({
            "name": data['name'],
            "department": data['department'],
            "roll_no": data['roll_no'],
            "sport": data['sport'],
            "type": "single",
            "user_id": auth_response.user.id
        }).execute()
        
        return jsonify({"success": True, "message": "Registration successful!"})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

@player_bp.route('/api/register-team', methods=['POST'])
def register_team_api():
    data = request.get_json()
    
    # Insert team
    team_response = supabase.table('teams').insert({
        "team_name": data['team_name'],
        "department": data['department'],
        "sport": data['sport']
    }).execute()
    
    team_id = team_response.data[0]['id']
    
    # Insert team players
    for player in data['players']:
        supabase.table('team_players').insert({
            "team_id": team_id,
            "name": player['name'],
            "roll_no": player['roll_no']
        }).execute()
    
    return jsonify({"success": True, "message": "Team registered!"})