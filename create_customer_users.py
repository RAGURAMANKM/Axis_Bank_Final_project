import pandas as pd
from sqlalchemy import text

from database import engine

# ----------------------------
# Read Customers
# ----------------------------

customers = pd.read_sql(
    "SELECT * FROM customers",
    engine
)

print("Customers Found:", len(customers))

count = 0

with engine.begin() as conn:

    for _, row in customers.iterrows():

        username = str(row["account_number"])

        password = username[-4:]      # Last 4 digits

        role = "customer"

        branch = row["branch"]

        # Check existing user
        exists = conn.execute(

            text("""
                SELECT 1
                FROM users
                WHERE username=:u
            """),

            {
                "u": username
            }

        ).fetchone()

        if exists:
            continue

        conn.execute(

            text("""
                INSERT INTO users
                (
                    username,
                    password,
                    role,
                    branch
                )

                VALUES
                (
                    :username,
                    :password,
                    :role,
                    :branch
                )
            """),

            {
                "username": username,
                "password": password,
                "role": role,
                "branch": branch
            }

        )

        count += 1

print()
print("=" * 50)
print("Customer Accounts Created :", count)
print("=" * 50)
print()

print("Sample Login")
print("Username : 920000000001")
print("Password : 0001")