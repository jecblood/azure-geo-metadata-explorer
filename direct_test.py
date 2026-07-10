# direct_test.py

import pyodbc

conn_str = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=SERVER;"
    "DATABASE=DATABASE_NAME;"
    "UID=YOUR_USERNAME;"
    "PWD=YOUR_PASSWORD;"
    "Encrypt=yes;"
    "TrustServerCertificate=no;"
)

print("Attempting connection...")

conn = pyodbc.connect(conn_str)

print("SUCCESS!")

conn.close()
