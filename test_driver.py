import pyodbc

print("Available drivers:")
print(pyodbc.drivers())

conn_str = (
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=SERVER;"
    "DATABASE=DATABASE_NAME;"
    "UID=YOUR_USERNAME;"
    "PWD=YOUR_PASSWORD;"
    "Encrypt=yes;"
    "TrustServerCertificate=no;"
)
