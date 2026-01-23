# backend/seed_db.py
from config import supabase

def seed_database():
    # Check if admin exists
    admin_check = supabase.table('profiles').select('*').eq('email', 'admin1@example.com').execute()
    if not admin_check.data:
        print("🌱 Creating admin user...")
        try:
            # Create auth user
            admin_auth = supabase.auth.sign_up({
                "email": "admin1@example.com",
                "password": "admin123"
            })
            # Create profile
            supabase.table('profiles').insert({
                "id": admin_auth.user.id,
                "email": "admin1@example.com",
                "role": "admin"
            }).execute()
            print("✅ Admin user created")
        except Exception as e:
            print(f"⚠️ Admin creation failed: {e}")
    
    # Check if coordinator exists
    coord_check = supabase.table('profiles').select('*').eq('email', 'coord1@example.com').execute()
    if not coord_check.data:
        print("🌱 Creating coordinator user...")
        try:
            coord_auth = supabase.auth.sign_up({
                "email": "coord1@example.com",
                "password": "coord123"
            })
            supabase.table('profiles').insert({
                "id": coord_auth.user.id,
                "email": "coord1@example.com",
                "role": "coord"
            }).execute()
            print("✅ Coordinator user created")
        except Exception as e:
            print(f"⚠️ Coordinator creation failed: {e}")