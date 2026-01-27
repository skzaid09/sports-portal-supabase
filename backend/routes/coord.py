# backend/routes/coord.py
from flask import Blueprint, render_template, session, redirect, jsonify, request
from config import supabase
from datetime import datetime

coord_bp = Blueprint('coord', __name__)

@coord_bp.route('/login')
def login():
    return render_template('coord/login.html')

@coord_bp.route('/dashboard')
def dashboard():
    if 'user' not in session or session['user']['role'] != 'coord':
        return redirect('/coord/login')

    matches_response = supabase.table('matches').select('*').execute()
    return render_template('coord/dashboard.html', matches=matches_response.data)

@coord_bp.route('/api/schedule-match', methods=['POST'])
def schedule_match():
    if 'user' not in session or session['user']['role'] != 'coord':
        return jsonify({"success": False, "message": "Unauthorized"}), 403

    data = request.get_json()
    supabase.table('matches').insert({
        "event": data['event'],
        "team1": data['team1'],
        "team2": data['team2'],
        "date": data['date'],
        "status": "Scheduled"
    }).execute()

    return jsonify({"success": True})

@coord_bp.route('/logout')
def logout():
    session.clear()
    return redirect('/')
