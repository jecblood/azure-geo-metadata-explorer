import pandas as pd
import sqlite3

df = pd.read_csv(
    "data/gse41861_metadata.csv"
)

conn = sqlite3.connect("geo.db")

df.to_sql(
    "Samples",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("Loaded into SQLite")