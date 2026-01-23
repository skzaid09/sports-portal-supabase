# backend/config.py
import os
from supabase import create_client

SUPABASE_URL = os.environ.get('SUPABASE_URL') or "http://localhost:54321"
SUPABASE_KEY = os.environ.get('SUPABASE_KEY') or "your-local-anon-key"
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
