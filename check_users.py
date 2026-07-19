import pandas as pd
from database import engine

df = pd.read_sql(
    """
    SELECT user_id, username, role, branch
    FROM users
    """,
    engine
)

print(df)