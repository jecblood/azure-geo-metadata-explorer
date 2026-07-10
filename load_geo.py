import pandas as pd
import sqlite3

# Read CSV
df = pd.read_csv("data/gse41861_metadata.csv")

print("Loaded data:")
print(df.head())

# Connect to SQLite
conn = sqlite3.connect("geo.db")

# Write dataframe to SQL table
df.to_sql(
    "Samples",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("\nData loaded into SQLite!")