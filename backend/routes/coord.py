# backend/routes/coord.py
from flask import Blueprint, render_template, session, redirect, url_for, request, jsonify
from config import supabase

coord_bp = Blueprint('coord', __name__)

@coord_bp.route('/login')
def login():
    return render_template('coord/login.html')

@coord_bp.route('/dashboard')
def dashboard():
    if 'user' not in session or session['user']['role'] != 'coord':
        return redirect('/')
    
    events_response = supabase.table('events').select('*').execute()
    matches_response = supabase.table('matches').select('*').execute()
    
    return render_template('coord/dashboard.html', 
                         events=events_response.data, 
                         matches=matches_response.data)

@coord_bp.route('/api/schedule-match', methods=['POST'])
def schedule_match():
    data = request.get_json()
    match = {
        "event": data['event'],
        "team1": data['team1'],
        "team2": data['team2'],
        "date": data['date'],
        "status": "scheduled"
    }
    supabase.table('matches').insert(match).execute()
    return jsonify({"success": True})