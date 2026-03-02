# # # # import os
# # # # from supabase import create_client

# # # # SUPABASE_URL = os.environ.get("SUPABASE_URL")
# # # # SUPABASE_SERVICE_KEY = os.environ.get("SUPABASE_SERVICE_KEY")

# # # # if not SUPABASE_URL or not SUPABASE_SERVICE_KEY:
# # # #     raise Exception("Missing Supabase environment variables!")

# # # # supabase = create_client(SUPABASE_URL, SUPABASE_SERVICE_KEY)

# # # # SECRET_KEY = os.environ.get("SECRET_KEY", "dev_secret")

# # # 222

# # import os
# # from supabase import create_client

# # SUPABASE_URL = os.getenv("SUPABASE_URL")
# # SUPABASE_SERVICE_KEY = os.getenv("SUPABASE_SERVICE_KEY")

# # # Debug print (remove after submission)
# # print("SUPABASE_URL:", SUPABASE_URL)
# # print("SERVICE_KEY present:", bool(SUPABASE_SERVICE_KEY))

# # if not SUPABASE_URL or not SUPABASE_SERVICE_KEY:
# #     raise Exception("Supabase environment variables missing!")

# # supabase = create_client(SUPABASE_URL, SUPABASE_SERVICE_KEY)

# # 3

# import os
# from supabase import create_client, Client

# SUPABASE_URL = os.getenv("SUPABASE_URL")
# SUPABASE_SERVICE_KEY = os.getenv("SUPABASE_SERVICE_KEY")

# if not SUPABASE_URL or not SUPABASE_SERVICE_KEY:
#     raise Exception("Supabase ENV missing!")

# supabase: Client = create_client(SUPABASE_URL, SUPABASE_SERVICE_KEY)

# final fixed

import os
from supabase import create_client

SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_SERVICE_KEY = os.getenv("SUPABASE_SERVICE_KEY")

supabase = create_client(SUPABASE_URL, SUPABASE_SERVICE_KEY)