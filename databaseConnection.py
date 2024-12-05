import mysql.connector
from mysql.connector import errorcode
from dotenv import load_dotenv
import os


# Load environment variables from .env file
load_dotenv()

class DatabaseConnection:
    def __init__(self):
        # Initialize connection and cursor attributes for later use.
        self.connection = None
        self.cursor = None

    def get_cursor(self):
        if self.connection and self.connection.is_connected():
            self.cursor = self.connection.cursor()
            return self.cursor
        else:
            print("Not connected to the database.")
            return None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                user=os.getenv('DB_USER'),
                password=os.getenv('DB_PASSWORD'),
                host=os.getenv('DB_HOST'),
                database=os.getenv('DB_NAME'),
                port=int(os.getenv('DB_PORT', 3306))  # Default to 3306
            )

        except mysql.connector.Error as db_error:
            if db_error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Invalid username or password.")
            elif db_error.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist.")
            else:
                print(f"Error: {db_error}")
            raise  # Re-raise exception after logging
            

    def execute_query(self, query, parameters=None):
        try:
            cursor = self.get_cursor()
            if not cursor:
                raise ValueError("Cannot execute query without a database connection.")

            # Execute the query with or without parameters
            if parameters:
                cursor.execute(query, parameters)
            else:
                cursor.execute(query)

            # For SELECT queries, fetch and return results
            if query.strip().upper().startswith("SELECT"):
                results = cursor.fetchall()
                return results

            # For non-SELECT queries, commit changes
            self.connection.commit()

        except Exception:
            print("Something went wrong... here")
            self.connection.rollback()  # Rollback in case of error
            raise


    def close_connection(self):
        # Close the database connection.
        if self.connection and self.connection.is_connected():
            self.connection.close()
        else:
            print("There is no open connection to DB.")

    def __enter__(self):
        # This allows us to use 'with' statement for queries.
        self.connect()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # Ensure the connection is closed after using it.
        self.close_connection()
