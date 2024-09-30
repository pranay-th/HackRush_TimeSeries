import pandas as pd
from sqlalchemy import create_engine

# Replace with your DATABASE_URL
DATABASE_URL = "postgresql://neondb_owner:Ijov0mkf6Ohl@ep-damp-dust-a11bi2qp-pooler.ap-southeast-1.aws.neon.tech/neondb?sslmode=require"

# Create the SQLAlchemy engine for PostgreSQL
engine = create_engine(DATABASE_URL)

# Define a function to load CSV data into PostgreSQL
def load_csv_to_db(csv_file, table_name):
    try:
        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(csv_file)

        # Upload the data to the PostgreSQL table
        df.to_sql(table_name, engine, if_exists='append', index=False)
        print(f"Data from {csv_file} inserted successfully into {table_name}.")
    except Exception as e:
        print(f"Error: {e}")

# List of CSV files and corresponding table names
csv_files = ["r1.csv","r2.csv", "r3.csv"]  # Replace with your actual file paths
table_name = "Disease_Freq"  # Replace with your actual table names

# Loop through each CSV file and upload the data
for csv_file in csv_files:
    load_csv_to_db(csv_file, table_name)
