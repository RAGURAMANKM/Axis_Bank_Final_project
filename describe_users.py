import pandas as pd
from database import engine

query = """
SELECT column_name, data_type
FROM information_schema.columns
WHERE table_name = 'users'
ORDER BY ordinal_position;
"""

df = pd.read_sql(query, engine)

print(df)