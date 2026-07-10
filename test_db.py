import sqlite3

conn = sqlite3.connect("geo.db")

cursor = conn.cursor()

cursor.execute("""
INSERT INTO Samples
VALUES ('GSM002', 'GSE41861', 'Control')
""")

cursor.execute("""
INSERT INTO Samples
VALUES ('GSM003', 'GSE41861', 'Asthma')
""")

cursor.execute("""
INSERT INTO Samples
VALUES ('GSM004', 'GSE41861', 'Control')
""")

conn.commit()

print("Rows inserted!")

conn.close()