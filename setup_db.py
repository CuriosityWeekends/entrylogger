'''
Run This Script To Set-Up Te entire Database Structure
'''

from supabase import create_client, Client
from dotenv import load_dotenv
import os

load_dotenv()
url = os.getenv("SUPABASE_URL")
key = os.getenv("SUPABASE_KEY")

if not url or not key:
    raise Exception("Missing required environment variables: SUPABASE_URL and SUPABASE_KEY")
supabase: Client = create_client(url, key)

with open("schema.sql", "r") as file:
    schema_sql = file.read()

response= supabase.schema("public").rpc("sql", schema_sql)
print(response)
if response:
    print("✅ Schema initialized successfully.")
else:
    print(f"❌ Failed to initialize schema. Response: {response}")
