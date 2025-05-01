'''
Run This Script To Set-Up Te entire Database Structure
'''

import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

db_url = os.getenv("SUPABASE_DB_URL")
if not db_url:
    raise Exception("Missing SUPABASE_DB_URL in .env")

try:
    conn = psycopg2.connect(db_url)
    conn.autocommit = True  # So that CREATE statements take effect immediately

    with conn.cursor() as cur:
        with open("discord_schema.sql", "r") as file:
            schema_sql = file.read()
            cur.execute(schema_sql)
            print("✅ Schema applied successfully.")

except Exception as e:
    print(f"❌ Error: {e}")
finally:
    if 'conn' in locals():
        conn.close()
