from sqlalchemy import create_engine

server = "jeff-geo-sql-server.database.windows.net"
database = "geo_metadata_db"
username = "jecblood"
password = "Jfdnfn11!"

connection_string = (
    f"mssql+pyodbc://{username}:{password}"
    f"@{server}:1433/{database}"
    "?driver=ODBC+Driver+18+for+SQL+Server"
    "&Encrypt=yes"
    "&TrustServerCertificate=no"
)

engine = create_engine(connection_string)

with engine.connect() as conn:
    print("Connected to Azure SQL!")