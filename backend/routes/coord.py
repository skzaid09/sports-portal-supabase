from flask import Blueprint, render_template, session, redirect, request, jsonify
from backend.config import supabase

coord_bp = Blueprint('coord', __name__)

@coord_bp.route('/login')
def login():
    return render_template('coord/login.html')

@coord_bp.route('/dashboard')
def dashboard():
    if 'user' not in session or session['user']['role'] != 'coord':
        return redirect('/')

    matches = supabase.table('matches').select('*').execute().data
    return render_template('coord/dashboard.html', matches=matches)

@coord_bp.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@coord_bp.route('/api/schedule-match', methods=['POST'])
def schedule_match():
    data = request.get_json()
    supabase.table('matches').insert(data).execute()
    return jsonify(success=True)
