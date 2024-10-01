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

def update_city_count(city, date):
    valid_cities = ['Kolkata', 'Delhi', 'Pune']
    if city not in valid_cities:
        print(f"Error: {city} is not a valid city. Please choose from {', '.join(valid_cities)}.")
        return

    try:
        # SQL query to update the count
        update_query = f"""
        UPDATE "{city}"
        SET count = count + 1
        WHERE date = %s;
        """
        
        # Execute the query
        cursor.execute(update_query, (date,))
        
        # Commit the transaction
        connection.commit()
        
        print(f"Successfully updated count for {city} on {date}")
    except psycopg2.Error as e:
        print(f"Error updating count: {e}")
        connection.rollback()

# Example usage:
update_city_count('Delhi', '-05-15')
