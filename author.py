from databaseConnection import DatabaseConnection
import tabulate



class Author:
    def __init__(self, author_id=None, author_full_name=None):
        self.author_id = author_id
        self.author_full_name = author_full_name

    def addAuthor(self):
        try:
            query = "INSERT INTO authors (author_full_name) VALUES (%s)"
            params = (self.author_full_name)
            with DatabaseConnection() as db:
                db.execute_query(query, params)
                print("Author added successfully.")
        except Exception as e:
            print(f"Error adding author: {e}")


    def updateAuthor(self):
        try:
            query = "UPDATE authors SET author_full_name = %s WHERE id = %s"
            params = (self.author_full_name, self.author_id)
            with DatabaseConnection() as db:
                db.execute_query(query, params)
                print("Author updated successfully.")
        except Exception as e:
            print(f"Error updating author: {e}")

    def deleteAuthor(self):
        try:
            query = "DELETE FROM authors WHERE id = %s"
            params = (self.author_id,)
            with DatabaseConnection() as db:
                db.execute_query(query, params)
                print("Author deleted successfully.")
        except Exception as e:
            print(f"Error deleting author: {e}")

    # Doesn't need parameters so we make it a static method
    @staticmethod
    def listAuthors():
        query = "SELECT * FROM authors ORDER BY id"
        try:
            with DatabaseConnection() as db:
                authors = db.execute_query(query)
                # Prepare the data for tabulation
                headers = ["ID", "First Name", "Last Name"]
                # We gather table information as a tuple
                author_data = [(author[0], author[1]) for author in authors]

                # Use tabulate to format and print the table
                # fmt is the format of the table, meaning how it looks.
                print(tabulate.tabulate(author_data, headers=headers, tablefmt="pretty"))
        except Exception as e:
            print(f"Error listing authors: {e}")




