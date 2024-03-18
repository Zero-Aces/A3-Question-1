# db_connection.py
import psycopg2

def get_database_connection():
    """Establishes connection to the PostgreSQL database."""
    try:
        connection = psycopg2.connect(
            dbname='Tester', 
            user='postgres', 
            password='postgres', 
            host='localhost'
        )
        return connection
    except Exception as error:
        print(f"Failed to connect to the database due to: {error}")
