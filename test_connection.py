from database import engine

try:
    conn = engine.connect()
    print("=" * 50)
    print("CONNECTED TO RENDER POSTGRESQL")
    print("=" * 50)
    conn.close()

except Exception as e:
    print(e)