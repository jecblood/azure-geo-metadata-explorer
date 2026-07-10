import sqlite3

conn = sqlite3.connect("geo.db")

query = """
SELECT Disease,
       COUNT(*) as NumberSamples
FROM Samples
GROUP BY Disease
"""

results = conn.execute(query)

for row in results:
    print(row)

conn.close()