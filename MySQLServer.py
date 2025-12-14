import mysql.connector

def create_connection(host_name, user_name, user_password):
    """Create alx_book_store databse if not exists and return the connection object."""
    conn = None
    try:
        conn = mysql.connector.connect(
                host=host_name,
                user=user_name,
                password=user_password,
        )

        if conn.is_connected():
            cursor = conn.cursor()

            # Crreate database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

            print("Database 'alx_book_store' created sucessfully")

            cursor.close()

    except mysql.connector.Error as e:
        # Handles connection errors
        print(f"Error connecting to MYSQL: {e}")

    finally:
        # Close the connection
        if conn and conn.is_connected():
            conn.close()
            print("MySQL connection closed.")


if __name__== "__main__":
    create_connection("localhost", "root", "emmyprime55@mysqldb")