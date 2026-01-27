from flask import Blueprint, render_template, session, redirect, request, jsonify
from backend.config import supabase

admin_bp = Blueprint('admin', __name__)

@admin_bp.route('/login')
def login():
    return render_template('admin/login.html')

@admin_bp.route('/dashboard')
def dashboard():
    if 'user' not in session or session['user']['role'] != 'admin':
        return redirect('/')

    users = supabase.table('users').select('*').execute().data
    return render_template('admin/dashboard.html', users=users)

@admin_bp.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@admin_bp.route('/api/delete-user', methods=['POST'])
def delete_user():
    data = request.get_json()
    supabase.table('users').delete().eq('email', data['username']).execute()
    return jsonify(success=True)
