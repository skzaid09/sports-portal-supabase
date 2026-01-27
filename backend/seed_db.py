from config import supabase

def seed():
    users = [
        {"email": "admin1@example.com", "password": "admin123", "role": "admin"},
        {"email": "coord1@example.com", "password": "coord123", "role": "coord"},
    ]

    for u in users:
        exists = supabase.table("users").select("*").eq("email", u["email"]).execute()
        if exists.data:
            continue

        auth = supabase.auth.sign_up({
            "email": u["email"],
            "password": u["password"]
        })

        supabase.table("users").insert({
            "email": u["email"],
            "role": u["role"],
            "user_id": auth.user.id
        }).execute()

        print("✅ Created:", u["email"])

if __name__ == "__main__":
    seed()
