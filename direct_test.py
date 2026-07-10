# direct_test.py

import pyodbc

conn_str = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=jeff-geo-sql-server.database.windows.net;"
    "DATABASE=geo_metadata_db;"
    "UID=jecblood;"
    "PWD=Jfdnfn11!;"
    "Encrypt=yes;"
    "TrustServerCertificate=no;"
)

print("Attempting connection...")

conn = pyodbc.connect(conn_str)

print("SUCCESS!")

conn.close()