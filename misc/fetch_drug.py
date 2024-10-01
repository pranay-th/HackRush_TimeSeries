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
# Fetch data from Drug_Sales table
cursor.execute("""
SELECT "diseaseId", "date", "regionId", "salesCount"
FROM "Drug_Sales";
""")
drug_sales_data = pd.DataFrame(cursor.fetchall(), columns=['diseaseId', 'date', 'regionId', 'salesCount'])

print("Drug Sales Data:\n", drug_sales_data)

