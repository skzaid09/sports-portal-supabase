# backend/routes/admin.py
from flask import Blueprint, render_template, session, redirect, url_for
from config import supabase

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/login')
def login():
    return render_template('admin/login.html')

@admin_bp.route('/dashboard')
def dashboard():
    if 'user' not in session or session['user']['role'] != 'admin':
        return redirect('/')
    
    # Fetch all users
    profiles_response = supabase.table('profiles').select('*').execute()
    all_users = profiles_response.data
    
    return render_template('admin/dashboard.html', users=all_users)