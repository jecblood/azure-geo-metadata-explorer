# azure-geo-metadata-explorer
Cloud-based exploration of public NIH GEO datasets using Azure SQL Database, Azure Blob Storage, Python, and SQL.
# Azure GEO Metadata Explorer

## Overview

Azure GEO Metadata Explorer is a cloud-based data ingestion and analysis project that demonstrates how publicly available NIH Gene Expression Omnibus (GEO) datasets can be extracted, transformed, stored, and queried using Python, SQL, and Azure SQL Database.

This project uses the GEO dataset **GSE41861** as an example and walks through the process of:

1. Downloading GEO metadata with GEOparse
2. Converting metadata into a pandas DataFrame
3. Exporting metadata to CSV
4. Creating a relational database schema
5. Loading metadata into Azure SQL Database
6. Querying the data with SQL

The project was created as a hands-on exercise for learning:

- Azure SQL Database
- Cloud database administration
- SQL fundamentals
- Data ingestion workflows
- GitHub project management
- Azure Fundamentals (AZ-900) concepts

---

## Technologies

- Python 3
- GEOparse
- pandas
- SQLite
- Azure SQL Database
- SQL
- GitHub

---

## Project Architecture

```text
NIH GEO Dataset (GSE41861)
            |
            v
        GEOparse
            |
            v
      pandas DataFrame
            |
            v
      CSV Export
            |
            v
    Azure SQL Database
            |
            v
       SQL Queries
```

---

## Dataset

This project uses metadata derived from:

**GSE41861**

A publicly available GEO study containing nasal epithelial brushing samples.

Source:

https://www.ncbi.nlm.nih.gov/geo/

---

## Repository Structure

```text
azure-geo-metadata-explorer/

├── README.md
├── geo_to_csv.py
├── csv_to_sql.py
├── load_geo.py
├── query_db.py
├── test_db.py
│
├── data/
│   └── gse41861_metadata.csv
│
├── sql/
│   ├── create_tables.sql
│   └── example_queries.sql
│
└── screenshots/
    ├── azure-sql-server.png
    ├── database-schema.png
    └── sample-query-results.png
```

---

## Setup

### Clone Repository

```bash
git clone https://github.com/jecblood/azure-geo-metadata-explorer.git

cd azure-geo-metadata-explorer
```

### Create Conda Environment

```bash
conda create -n az900 python=3.12
conda activate az900
```

### Install Dependencies

```bash
pip install GEOparse pandas
```

---

## Download GEO Metadata

Example:

```python
import GEOparse

gse = GEOparse.get_GEO(
    geo="GSE41861",
    destdir="data"
)
```

Metadata are extracted into a pandas DataFrame and exported as:

```text
data/gse41861_metadata.csv
```

---

## Azure SQL Database

The project uses Azure SQL Database as a managed cloud database service (PaaS).

### Sample Table

```sql
CREATE TABLE dbo.Samples (
    SampleID NVARCHAR(50) PRIMARY KEY,
    Title NVARCHAR(255),
    Source NVARCHAR(MAX)
);
```

---

## Example SQL Queries

### Count Samples

```sql
SELECT COUNT(*) AS TotalSamples
FROM dbo.Samples;
```

### View Sample Records

```sql
SELECT TOP 10 *
FROM dbo.Samples;
```

### Search Metadata

```sql
SELECT *
FROM dbo.Samples
WHERE Title LIKE '%AA%';
```

### Count Unique Titles

```sql
SELECT COUNT(DISTINCT Title)
FROM dbo.Samples;
```

---

## Data Source

This project uses publicly available metadata from the NIH Gene Expression Omnibus (GEO):

GSE41861: Upper airway gene expression is an effective surrogate biomarker for Th2-driven inflammation in the lower airway.

Source:
https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE41861
