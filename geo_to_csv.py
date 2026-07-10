import GEOparse
import pandas as pd

gse = GEOparse.get_GEO(
    geo="GSE41861",
    destdir="data"
)

rows = []

for gsm_name, gsm in gse.gsms.items():

    rows.append({
        "SampleID": gsm_name,
        "Title": gsm.metadata.get("title", [""])[0],
        "Source": gsm.metadata.get("source_name_ch1", [""])[0]
    })

df = pd.DataFrame(rows)

print(df.head())

df.to_csv(
    "data/gse41861_metadata.csv",
    index=False
)

print("Saved metadata CSV")