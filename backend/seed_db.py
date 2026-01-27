from config import supabase

def seed():
    users = supabase.table("users").select("*").execute().data
    if not users:
        supabase.table("users").insert([
            {"email": "admin@sports.com", "role": "admin"},
            {"email": "coord@sports.com", "role": "coord"}
        ]).execute()

if __name__ == "__main__":
    seed()
