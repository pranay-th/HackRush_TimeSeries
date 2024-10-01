import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError

# Replace with your DATABASE_URL
DATABASE_URL = "postgresql://neondb_owner:Ijov0mkf6Ohl@ep-damp-dust-a11bi2qp-pooler.ap-southeast-1.aws.neon.tech/neondb?sslmode=require"

# Create the SQLAlchemy engine for PostgreSQL
engine = create_engine(DATABASE_URL)

# Define a function to load CSV data into PostgreSQL
def load_csv_to_db(csv_file, table_name):
    try:
        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(csv_file)

        # If 'id' column exists, drop it to let the database auto-generate ids
        if 'id' in df.columns:
            df = df.drop('id', axis=1)

        # Upload the data to the PostgreSQL table
        df.to_sql(table_name, engine, if_exists='append', index=False)
        print(f"Data from {csv_file} inserted successfully into {table_name}.")
    except IntegrityError as e:
        print(f"Error: Some records already exist in the database. {e}")
    except Exception as e:
        print(f"Error: {e}")

# List of CSV files and corresponding table names
csv_files = ["Extended_Drug_Sales.csv"]  # Replace with your actual file paths
table_names = ["Drug_Sales"]  # Replace with your actual table names

# Loop through each CSV file and upload the data
for csv_file, table_name in zip(csv_files, table_names):
    load_csv_to_db(csv_file, table_name)
