import GEOparse

gse = GEOparse.get_GEO(
    geo="GSE41861",
    destdir="data"
)

print("Number of samples:", len(gse.gsms))

#see what metadata fields are available
for gsm_name, gsm in gse.gsms.items():
    print(gsm_name)
    print(gsm.metadata.keys())
    break
