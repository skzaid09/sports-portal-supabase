# # # # # # # import os
# # # # # # # from supabase import create_client

# # # # # # # SUPABASE_URL = os.environ.get("SUPABASE_URL")
# # # # # # # SUPABASE_SERVICE_KEY = os.environ.get("SUPABASE_SERVICE_KEY")

# # # # # # # if not SUPABASE_URL or not SUPABASE_SERVICE_KEY:
# # # # # # #     raise Exception("Missing Supabase environment variables!")

# # # # # # # supabase = create_client(SUPABASE_URL, SUPABASE_SERVICE_KEY)

# # # # # # # SECRET_KEY = os.environ.get("SECRET_KEY", "dev_secret")

# # # # # # 222

# # # # # import os
# # # # # from supabase import create_client

# # # # # SUPABASE_URL = os.getenv("SUPABASE_URL")
# # # # # SUPABASE_SERVICE_KEY = os.getenv("SUPABASE_SERVICE_KEY")

# # # # # # Debug print (remove after submission)
# # # # # print("SUPABASE_URL:", SUPABASE_URL)
# # # # # print("SERVICE_KEY present:", bool(SUPABASE_SERVICE_KEY))

# # # # # if not SUPABASE_URL or not SUPABASE_SERVICE_KEY:
# # # # #     raise Exception("Supabase environment variables missing!")

# # # # # supabase = create_client(SUPABASE_URL, SUPABASE_SERVICE_KEY)

# # # # # 3

# # # # import os
# # # # from supabase import create_client, Client

# # # # SUPABASE_URL = os.getenv("SUPABASE_URL")
# # # # SUPABASE_SERVICE_KEY = os.getenv("SUPABASE_SERVICE_KEY")

# # # # if not SUPABASE_URL or not SUPABASE_SERVICE_KEY:
# # # #     raise Exception("Supabase ENV missing!")

# # # # supabase: Client = create_client(SUPABASE_URL, SUPABASE_SERVICE_KEY)

# # # # final fixed

# # # import os
# # # from supabase import create_client

# # # SUPABASE_URL = os.getenv("SUPABASE_URL")
# # # SUPABASE_SERVICE_KEY = os.getenv("SUPABASE_SERVICE_KEY")

# # # supabase = create_client(SUPABASE_URL, SUPABASE_SERVICE_KEY)
# # import os
# # import requests
# # from dotenv import load_dotenv

# # load_dotenv()

# # SUPABASE_URL = os.getenv("SUPABASE_URL")
# # SUPABASE_SERVICE_KEY = os.getenv("SUPABASE_SERVICE_KEY")

# # HEADERS = {
# #     "apikey": SUPABASE_SERVICE_KEY,
# #     "Authorization": f"Bearer {SUPABASE_SERVICE_KEY}",
# #     "Content-Type": "application/json"
# # }

# import os
# from dotenv import load_dotenv

# load_dotenv()

# SUPABASE_URL = os.getenv("SUPABASE_URL")
# SUPABASE_SERVICE_KEY = os.getenv("SUPABASE_SERVICE_KEY")

# HEADERS = {
#     "apikey": SUPABASE_SERVICE_KEY,
#     "Authorization": f"Bearer {SUPABASE_SERVICE_KEY}",
#     "Content-Type": "application/json"
# }

# new code

import os
import requests
from dotenv import load_dotenv

# Load .env
load_dotenv()

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_SERVICE_KEY = os.getenv("SUPABASE_SERVICE_KEY")

if not SUPABASE_URL or not SUPABASE_SERVICE_KEY:
    raise Exception("Supabase ENV variables missing!")

# Common headers
HEADERS = {
    "apikey": SUPABASE_SERVICE_KEY,
    "Authorization": f"Bearer {SUPABASE_SERVICE_KEY}",
    "Content-Type": "application/json"
}

# -------------------------
# FUNCTION 1 → Insert Match
# -------------------------
def insert_match(event, team1, team2, date):
    try:
        payload = {
            "event": event,
            "team1": team1,
            "team2": team2,
            "date": date,
            "status": "Scheduled"
        }

        url = f"{SUPABASE_URL}/rest/v1/matches"
        response = requests.post(url, headers=HEADERS, json=payload)

        return response.status_code == 201

    except Exception as e:
        print("Insert Error:", e)
        return False


# -------------------------
# FUNCTION 2 → Fetch Matches
# -------------------------
def get_all_matches():
    try:
        url = f"{SUPABASE_URL}/rest/v1/matches?select=*"
        response = requests.get(url, headers=HEADERS)

        if response.status_code == 200:
            return response.json()
        else:
            return []

    except Exception as e:
        print("Fetch Error:", e)
        return []