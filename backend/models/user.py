# backend/models/user.py
from config import supabase

def get_user_by_email(email):
    try:
        # Check if user exists in auth.users
        auth_user = supabase.auth.admin.get_user_by_email(email)
        if not auth_user:
            return None
            
        # Get role from profiles table
        profile_response = supabase.table('profiles').select('role').eq('email', email).execute()
        if profile_response.data and len(profile_response.data) > 0:
            return {
                "id": auth_user.id,
                "email": email,
                "role": profile_response.data[0]['role']
            }
        else:
            return None
    except Exception as e:
        print(f"Error fetching user: {e}")
        return None