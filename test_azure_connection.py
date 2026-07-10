from sqlalchemy import create_engine

server = "SERVER"
database = "DATABASE_NAME"
username = "YOUR_USERNAME"
password = "YOUR_PASSWORD"

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
