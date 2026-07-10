# csv_to_sql.py

import pandas as pd

df = pd.read_csv("data/gse41861_metadata.csv")

with open("import_samples.sql", "w") as f:

    for _, row in df.iterrows():

        sample = str(row["SampleID"]).replace("'", "''")
        title = str(row["Title"]).replace("'", "''")
        source = str(row["Source"]).replace("'", "''")

        f.write(
            f"INSERT INTO dbo.Samples "
            f"(SampleID, Title, Source) "
            f"VALUES ('{sample}','{title}','{source}');\n"
        )

print("Created import_samples.sql")