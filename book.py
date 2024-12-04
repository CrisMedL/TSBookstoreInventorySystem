from databaseConnection import DatabaseConnection
import tabulate

class Book:
    def __init__(self, book_id=None, book_title=None, genre_id=None, author_id=None, price = None, stock_quantity = None):
        self.book_id = book_id
        self.book_title = book_title
        self.genre_id = genre_id
        self.author_id = author_id
        self.price = price
        self.stock_quantity = stock_quantity

    def addBook(self):
        query = "INSERT INTO books (title,genre_id, author_id, price, stock_quantity) VALUES (%s,%s,%s,%s,%s,%s)"
        params = ()
        try:
            with DatabaseConnection() as db:
                db.execute_query(query, params)
                print("Author added successfully.")
        except Exception as e:
            print(f"Error adding author: {e}")


    def updateBook(self):
        try:
            author_id = input("Choose which author to update (Enter id): ")
            first_name = input("Input author's first name: ").strip().capitalize()
            last_name = input("Input author's last name: ").strip().capitalize()
        except ValueError:
            print("Invalid input. Please enter a valid name.")
            return
        query = "UPDATE authors SET first_name=%s, last_name=%s WHERE id=%s"
        params = (first_name, last_name, author_id)
        try:
            with DatabaseConnection() as db:
                db.execute_query(query, params)
                print("Author updated successfully.")
        except Exception as e:
            print(f"Error updating author: {e}")


    def deleteBook(self):
        author_id = input("Choose which author to delete (Enter id): ")
        query = "DELETE FROM authors WHERE id = %s"
        params = (author_id)
        try:
            with DatabaseConnection() as db:
                db.execute_query(query, params)
                print("Author deleted successfully.")
        except Exception as e:
            print(f"Error deleting author: {e}")

    # Doesn't need parameters so we make it a static method
    @staticmethod
    def listBooks():
        query = "SELECT * FROM books ORDER BY id"
        try:
            with DatabaseConnection() as db:
                books = db.execute_query(query)
                
                # Prepare the data for tabulation
                headers = ["ID", "Book Title", "Genre", "Author", "Original Price", "Discount Price", "Has a Discount", "Discount Type", "Stock"]  # Table headers
                # We gather table information as a tuple
                book_data = [(books[0], books[1], books[2], books[3], books[4], books[5], books[6], books[7], books[8]) for book in books] 

                # Use tabulate to format and print the table
                # fmt is the format of the table, meaning how it looks.
                print(tabulate.tabulate(book_data, headers=headers, tablefmt="pretty"))
        
        except Exception as e:
            print(f"Error listing books: {e}")

    # Doesn't need parameters so we make it a static method
    @staticmethod
    def listLowStockBooks():
        query = "SELECT * FROM books ORDER BY  "
        try:
            with DatabaseConnection() as db:
                books = db.execute_query(query)
                
                # Prepare the data for tabulation
                headers = ["ID", "First Name", "Last Name"]  # Table headers
                # We gather table information as a tuple
                book_data = [(books[0], books[1], books[2], books[3], books[4], books[5], books[6], books[7], books[8]) for book in books] 

                # Use tabulate to format and print the table
                # fmt is the format of the table, meaning how it looks.
                print(tabulate.tabulate(book_data, headers=headers, tablefmt="pretty"))
        
        except Exception as e:
            print(f"Error listing authors: {e}")

    
