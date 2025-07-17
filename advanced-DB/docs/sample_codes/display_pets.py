import os
from psycopg2 import pool, Error
from dotenv import load_dotenv

# Load .env file
load_dotenv('C:\\Users\\pnbay\\Nipe\\nipe\\advanced-DB\\docs\\sample_codes\\config.env')

# Get the connection string from the environment variable
connection_string = os.getenv('DATABASE_URL')
print("Connection string:", connection_string)

# Create a connection pool
try:
    connection_pool = pool.SimpleConnectionPool(
        1,  # Min connections
        10, # Max connections
        connection_string
    )
    if connection_pool:
        print("Connection pool created successfully!")

    # Fetch a connection from the pool
    conn = connection_pool.getconn()
    cursor = conn.cursor()

    # Example query
    cursor.execute("SELECT id, name, breed, age FROM pets ORDER BY age DESC;")
    rows = cursor.fetchall()

    print("\n🐾 List of Pets:")
    for row in rows:
        print(f"ID: {row[0]}, Name: {row[1]}, Breed: {row[2]}, Age: {row[3]}")

except Error as e:
    print("Database error:", e)

finally:
    # Return the connection back to the pool
    if 'conn' in locals():
        connection_pool.putconn(conn)
        print("\nReturned connection to the pool.")

    # Close pool if you're done with all queries
    if 'connection_pool' in locals() and connection_pool:
        connection_pool.closeall()
        print("Connection pool closed.")
