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
        supabase.table('profiles').insert({
            "id": auth_response.user.id,
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
            "user_id": auth_response.user.id,
            "created_at": str(datetime.utcnow())
        }).execute()
        
        return jsonify({"success": True, "message": "Registration successful!"})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500