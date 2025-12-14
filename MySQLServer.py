import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, db_name):
    """Create alx_book_store databse if not exists and return the connection object."""
    conn = None
    try:
        conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="emmyprime55@mysqldb"
        )

        if conn.is_connected():
            cursor = conn.cursor()

            # Crreate database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

            print("Database 'alx_book_store' created sucessfully")

            cursor.close()

    except Error as e:
        # Handles connection errors
        print(f"Error connecting to MYSQL: {e}")

    finally:
        # Close the connection
        if conn and conn.is_connected():
            conn.close()
            print("MySQL connection closed.")


if__name__=="__main__":
    create_database()
