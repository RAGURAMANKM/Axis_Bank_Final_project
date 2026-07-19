from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()

engine = create_engine(os.getenv("DATABASE_URL"))

with engine.begin() as conn:
    conn.execute(text("DROP TABLE IF EXISTS transactions CASCADE;"))
    conn.execute(text("DROP TABLE IF EXISTS customers CASCADE;"))

print("Tables dropped successfully.")