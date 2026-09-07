import sqlite3
import pandas as pd
import os

# File paths
csv_file = "data/processed/german_credit_clean.csv"
database_file = "data/final/credit_risk.db"

# Create final folder
os.makedirs("data/final", exist_ok=True)

# Load cleaned data
df = pd.read_csv(csv_file)

# Create SQLite database
connection = sqlite3.connect(database_file)

# Load dataframe into SQL table
df.to_sql(
    "credit_risk",
    connection,
    if_exists="replace",
    index=False
)

# Check number of rows
cursor = connection.cursor()
cursor.execute("SELECT COUNT(*) FROM credit_risk")
count = cursor.fetchone()[0]

print("=" * 50)
print("SQL DATABASE CREATED")
print("=" * 50)
print(f"Rows loaded: {count:,}")
print(f"Database: {database_file}")
print("Table: credit_risk")

connection.close()