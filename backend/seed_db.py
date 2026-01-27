# backend/seed_db.py
from config import supabase

def seed_database():
    # Seed admin user
    admin_email = "admin1@example.com"
    admin_password = "admin123"
    
    # Create auth user
    try:
        admin_auth = supabase.auth.admin.create_user({
            "email": admin_email,
            "password": admin_password,
            "email_confirm": True
        })
        
        # Create profile
        supabase.table('profiles').insert({
            "id": admin_auth.user.id,
            "email": admin_email,
            "role": "admin"
        }).execute()
        print("✅ Admin user created")
    except Exception as e:
        print(f"⚠️ Admin creation failed: {e}")

    # Seed coordinator user
    coord_email = "coord1@example.com"
    coord_password = "coord123"
    
    try:
        coord_auth = supabase.auth.admin.create_user({
            "email": coord_email,
            "password": coord_password,
            "email_confirm": True
        })
        
        supabase.table('profiles').insert({
            "id": coord_auth.user.id,
            "email": coord_email,
            "role": "coord"
        }).execute()
        print("✅ Coordinator user created")
    except Exception as e:
        print(f"⚠️ Coordinator creation failed: {e}")

    # Seed player user
    player_email = "player1@example.com"
    player_password = "player123"
    
    try:
        player_auth = supabase.auth.admin.create_user({
            "email": player_email,
            "password": player_password,
            "email_confirm": True
        })
        
        supabase.table('profiles').insert({
            "id": player_auth.user.id,
            "email": player_email,
            "role": "player"
        }).execute()
        print("✅ Player user created")
    except Exception as e:
        print(f"⚠️ Player creation failed: {e}")