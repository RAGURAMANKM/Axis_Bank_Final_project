import pandas as pd

from sqlalchemy import text

from database import engine


print("=" * 60)
print("Loading CSV files...")
print("=" * 60)


customers = pd.read_csv(
    "customers_extracted.csv",
    dtype=str
)

transactions = pd.read_csv(
    "transactions.csv"
)

print("Customers :", len(customers))
print("Transactions :", len(transactions))


with engine.begin() as conn:

    print("\nDropping old tables...")

    conn.execute(text("""
        DROP TABLE IF EXISTS transactions;
    """))

    conn.execute(text("""
        DROP TABLE IF EXISTS customers;
    """))

print("Old tables removed.")


print("\nCreating customers table...")

customers.to_sql(

    "customers",

    engine,

    if_exists="replace",

    index=False,

    method="multi",

    chunksize=1000

)

print("Customers inserted.")


print("\nCreating transactions table...")

transactions.to_sql(

    "transactions",

    engine,

    if_exists="replace",

    index=False,

    method="multi",

    chunksize=5000

)

print("Transactions inserted.")


print("\nCreating indexes...")

with engine.begin() as conn:

    conn.execute(text("""
        CREATE INDEX idx_customer_account
        ON customers(account_number);
    """))

    conn.execute(text("""
        CREATE INDEX idx_transaction_account
        ON transactions(account_number);
    """))

    conn.execute(text("""
        CREATE INDEX idx_transaction_date
        ON transactions(date);
    """))

print("Indexes created.")

print("\nDatabase Loaded Successfully.")