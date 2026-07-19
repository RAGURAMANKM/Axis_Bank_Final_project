import pandas as pd

from database import engine


customers = pd.read_sql(

    "SELECT COUNT(*) AS total FROM customers",

    engine

)

transactions = pd.read_sql(

    "SELECT COUNT(*) AS total FROM transactions",

    engine

)

print(customers)

print(transactions)