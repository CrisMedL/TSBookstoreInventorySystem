from databaseConnection import DatabaseConnection
import tabulate

class Book:
    def __init__(self, book_id=None, book_title=None, genre_id=None, author_id=None, price=None, stock_quantity=None):
        self.book_id = book_id
        self.book_title = book_title
        self.genre_id = genre_id
        self.author_id = author_id
        self.price = price
        self.stock_quantity = stock_quantity

    def addBook(self):
        query = "INSERT INTO books (title ,genre_id, author_id, price, stock_quantity) VALUES (%s,%s,%s,%s,%s,%s)"
        params = (self.book_title, self.genre_id, self.author_id, self.price, self.stock_quantity)
        try:
            with DatabaseConnection() as db:
                db.execute_query(query, params)
                print("Book added successfully.")
        except Exception as e:
            print(f"Error adding book: {e}")


    def updateBook(self):
        query = "UPDATE books SET title = %s, genre_id = %s, author_id = %s, price = %s, stock_quantity = %s WHERE id=%s"
        params = (self.title, self.genre_id, self.author_id, self.price, self.stock_quantity)
        try:
            with DatabaseConnection() as db:
                db.execute_query(query, params)
                print("Book updated successfully.")
        except Exception as e:
            print(f"Error updating book: {e}")


    def deleteBook(self):
        query = "DELETE FROM books WHERE id = %s"
        params = (self.book_id, ) # execute_query expects a tuple
        try:
            with DatabaseConnection() as db:
                db.execute_query(query, params)
                print("Book deleted successfully.")
        except Exception as e:
            print(f"Error deleting Book : {e}")

    # Doesn't need parameters so we make it a static method
    @staticmethod
    def listBooks():
        query = """SELECT books.id, books.title, genres.genre_name, authors.author_full_name, books.price, books.stock_quantity
                FROM books
                JOIN genres ON books.genre_id = genres.id
                JOIN authors ON books.author_id = authors.id
                ORDER BY books.id ASC"""
        try:
            with DatabaseConnection() as db:
                books = db.execute_query(query)
                
                # Prepare the data for tabulation
                headers = ["ID", "Book Title", "Genre", "Author", "Original Price ($)", "Stock"]  # Table headers
                # We gather table information as a tuple
                book_data = [(books[0], books[1], books[2], books[3], books[4], books[5]) for book in books] 

                # Use tabulate to format and print the table
                # fmt is the format of the table, meaning how it looks.
                print(tabulate.tabulate(book_data, headers=headers, tablefmt="pretty"))
        
        except Exception as e:
            print(f"Error listing books: {e}")

    # Doesn't need parameters so we make it a static method
    @staticmethod
    def sortBooksByStock():
        query = """SELECT books.id, books.title, genres.genre_name, authors.author_full_name, books.price, books.stock_quantity
                FROM books
                JOIN genres ON books.genre_id = genres.id
                JOIN authors ON books.author_id = authors.id
                ORDER BY books.stock_quantity ASC"""
        try:
            with DatabaseConnection() as db:
                books = db.execute_query(query)
                
                # Prepare the data for tabulation
                headers = ["ID", "Book Title", "Genre", "Author", "Original Price ($)", "Stock"]  # Table headers
                # We gather table information as a tuple
                book_data = [(books[0], books[1], books[2], books[3], books[4], books[5]) for book in books] 

                # Use tabulate to format and print the table
                # fmt is the format of the table, meaning how it looks.
                print(tabulate.tabulate(book_data, headers=headers, tablefmt="pretty"))
        
        except Exception as e:
            print(f"Error listing books: {e}")

    # Doesn't need parameters so we make it a static method
    @staticmethod
    def sortBooksByPrice():
        query = """SELECT books.id, books.title, genres.genre_name, authors.author_full_name, books.price, books.stock_quantity
                FROM books
                JOIN genres ON books.genre_id = genres.id
                JOIN authors ON books.author_id = authors.id
                ORDER BY books.stock_quantity ASC"""
        try:
            with DatabaseConnection() as db:
                books = db.execute_query(query)
                
                # Prepare the data for tabulation
                headers = ["ID", "Book Title", "Genre", "Author", "Original Price ($)", "Stock"]  # Table headers
                # We gather table information as a tuple
                book_data = [(books[0], books[1], books[2], books[3], books[4], books[5]) for book in books] 

                # Use tabulate to format and print the table
                # fmt is the format of the table, meaning how it looks.
                print(tabulate.tabulate(book_data, headers=headers, tablefmt="pretty"))
        
        except Exception as e:
            print(f"Error listing books: {e}")

    
