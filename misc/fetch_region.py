import psycopg2
import pandas as pd

# Connect to the Neon DB
connection = psycopg2.connect(
    # Check these parameters
    host="ep-damp-dust-a11bi2qp-pooler.ap-southeast-1.aws.neon.tech", 
    port="5432",
    database="neondb",
    user="neondb_owner",
    password="Ijov0mkf6Ohl",
    sslmode="require"
)

# Create a cursor object
cursor = connection.cursor()

cursor.execute("""
SELECT "ID", "Date", "Count", "Region ID", "Disease ID", "Disease", "Region"
FROM "Kolkata";
""")
kolkata_data = pd.DataFrame(cursor.fetchall(), columns=['ID', 'Date', 'Count', 'Region ID', 'Disease ID', 'Disease', 'Region'])

# Fetch data from Delhi table
cursor.execute("""
SELECT "ID", "Date", "Count", "Region ID", "Disease ID", "Disease", "Region"
FROM "Delhi";
""")
delhi_data = pd.DataFrame(cursor.fetchall(), columns=['ID', 'Date', 'Count', 'Region ID', 'Disease ID', 'Disease', 'Region'])

# Fetch data from Pune table
cursor.execute("""
SELECT "ID", "Date", "Count", "Region ID", "Disease ID", "Disease", "Region"
FROM "Pune";
""")
pune_data = pd.DataFrame(cursor.fetchall(), columns=['ID', 'Date', 'Count', 'Region ID', 'Disease ID', 'Disease', 'Region'])

print("Kolkata Data:\n", kolkata_data)
print("\nDelhi Data:\n", delhi_data)
print("\nPune Data:\n", pune_data)