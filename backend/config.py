import os
from supabase import create_client

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_SERVICE_KEY = os.environ.get("SUPABASE_SERVICE_KEY")

if not SUPABASE_URL or not SUPABASE_SERVICE_KEY:
    raise Exception("Missing Supabase environment variables!")

supabase = create_client(SUPABASE_URL, SUPABASE_SERVICE_KEY)

SECRET_KEY = os.environ.get("SECRET_KEY", "dev_secret")