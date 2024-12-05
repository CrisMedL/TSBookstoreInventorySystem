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
        query = "INSERT INTO books (title ,genre_id, author_id, price, stock_quantity) VALUES (%s,%s,%s,%s,%s)"
        params = (self.book_title, self.genre_id, self.author_id, self.price, self.stock_quantity)
        try:
            with DatabaseConnection() as db:
                db.execute_query(query, params)
                print("Book added successfully.")
        except Exception as e:
            print(f"Error adding book: {e}")

    def updateBookTitle(self):
        query = "UPDATE books SET title = %s WHERE id = %s"
        params = (self.book_title,self.book_id)
        try:
            with DatabaseConnection() as db:
                db.execute_query(query, params)
                print("Book updated successfully.")
        except Exception as e:
            print(f"Error updating book: {e}")
    
    def updateBookGenre(self):
        query = "UPDATE books SET genre_id = %s WHERE id = %s"
        params = (self.genre_id,self.book_id)
        try:
            with DatabaseConnection() as db:
                db.execute_query(query, params)
                print("Book updated successfully.")
        except Exception as e:
            print(f"Error updating book: {e}")

    def updateBookAuthor(self):
        query = "UPDATE books SET author_id = %s WHERE id = %s"
        params = (self.author_id,self.book_id)
        try:
            with DatabaseConnection() as db:
                db.execute_query(query, params)
                print("Book updated successfully.")
        except Exception as e:
            print(f"Error updating book: {e}")
    
    def updateBookPrice(self,book_id, price):
        query = "UPDATE books SET price = %s WHERE id = %s"
        params = (self.price,self.book_id)
        try:
            with DatabaseConnection() as db:
                db.execute_query(query, params)
                print("Book updated successfully.")
        except Exception as e:
            print(f"Error updating book: {e}")

    def updateBookStock(self):
        query = "UPDATE books SET stock_quantity = %s WHERE id = %s"
        params = (self.stock_quantity,self.book_id)
        try:
            with DatabaseConnection() as db:
                db.execute_query(query, params)
                print("Book updated successfully.")
        except Exception as e:
            print(f"Error updating book: {e}")

    def deleteBook(self):
        query = "DELETE FROM books WHERE id = %s"
        params = (self.book_id,) # execute_query expects a tuple
        try:
            with DatabaseConnection() as db:
                db.execute_query(query, params)
                print("Book deleted successfully.")
        except Exception as e:
            print(f"Error deleting Book : {e}")

    def fetchSingleBook(self):
        query = "SELECT * FROM books WHERE id = %s"
        params = (self.book_id,)
        try:
            with DatabaseConnection() as db:
                book = db.execute_query(query, params)

                if not book or len(book) == 0:
                    print(f"No book found with ID {self.book_id}.")
                    return None  # Explicitly return None if no book is found

                # Unpack the first row if a list of rows is returned otherwise this won't work
                if isinstance(book, list):
                    book = book[0]

                # Tabulate and display the data
                headers = ["ID", "Book Title", "Genre", "Author", "Price $", "Stock"]
                book_data = [(book[0], book[1], book[2], book[3], book[4], book[5])]
                print(tabulate.tabulate(book_data, headers=headers, tablefmt="pretty"))

                # Return the book data for further use
                return book

        except Exception as e:
            print(f"Error fetching book: {e}")
            return False


    # Doesn't need parameters so we make it a static method
    @staticmethod
    def listBooksByIdentifier():
        query = """SELECT books.id, books.title, genres.genre_name, authors.author_full_name, books.price, books.stock_quantity
                FROM books
                JOIN genres ON books.genre_id = genres.id
                JOIN authors ON books.author_id = authors.id
                ORDER BY books.id ASC"""
        try:
            with DatabaseConnection() as db:
                books = db.execute_query(query)
                
                # Prepare the data for tabulation
                headers = ["ID", "Book Title", "Genre", "Author", "Price $", "Stock"]  # Table headers
                # Process each book row
                book_data = [(book[0], book[1], book[2], book[3], book[4], book[5]) for book in books]

                # Use tabulate to format and print the table
                print(tabulate.tabulate(book_data, headers=headers, tablefmt="pretty"))
        
        except Exception as e:
            print(f"Error listing books: {e}")

    @staticmethod
    def listBooksByTitle():
        query = """SELECT books.id, books.title, genres.genre_name, authors.author_full_name, books.price, books.stock_quantity
                FROM books
                JOIN genres ON books.genre_id = genres.id
                JOIN authors ON books.author_id = authors.id
                ORDER BY books.stock_quantity ASC"""
        try:
            with DatabaseConnection() as db:
                books = db.execute_query(query)
                
                # Prepare the data for tabulation
                headers = ["ID", "Book Title", "Genre", "Author", "Price $", "Stock"]  # Table headers
                # Process each book row
                book_data = [(book[0], book[1], book[2], book[3], book[4], book[5]) for book in books]

                # Use tabulate to format and print the table
                print(tabulate.tabulate(book_data, headers=headers, tablefmt="pretty"))
        
        except Exception as e:
            print(f"Error listing books: {e}")

    @staticmethod
    def listBooksByAuthor():
        query = """SELECT books.id, books.title, genres.genre_name, authors.author_full_name, books.price, books.stock_quantity
                FROM books
                JOIN genres ON books.genre_id = genres.id
                JOIN authors ON books.author_id = authors.id
                ORDER BY authors.author_full_name ASC"""
        try:
            with DatabaseConnection() as db:
                books = db.execute_query(query)
                
                # Prepare the data for tabulation
                headers = ["ID", "Book Title", "Genre", "Author", "Price $", "Stock"]  # Table headers
                # Process each book row
                book_data = [(book[0], book[1], book[2], book[3], book[4], book[5]) for book in books]

                # Use tabulate to format and print the table
                print(tabulate.tabulate(book_data, headers=headers, tablefmt="pretty"))
        
        except Exception as e:
            print(f"Error listing books: {e}")

    # Doesn't need parameters so we make it a static method
    @staticmethod
    def listBooksByStock():
        query = """SELECT books.id, books.title, genres.genre_name, authors.author_full_name, books.price, books.stock_quantity
                FROM books
                JOIN genres ON books.genre_id = genres.id
                JOIN authors ON books.author_id = authors.id
                ORDER BY books.stock_quantity ASC"""
        try:
            with DatabaseConnection() as db:
                books = db.execute_query(query)
                
                # Prepare the data for tabulation
                headers = ["ID", "Book Title", "Genre", "Author", "Price $", "Stock"]  # Table headers
                # Process each book row
                book_data = [(book[0], book[1], book[2], book[3], book[4], book[5]) for book in books]

                # Use tabulate to format and print the table
                print(tabulate.tabulate(book_data, headers=headers, tablefmt="pretty"))
        
        except Exception as e:
            print(f"Error listing books: {e}")

    # Doesn't need parameters so we make it a static method
    @staticmethod
    def listBooksByPrice():
        query = """SELECT books.id, books.title, genres.genre_name, authors.author_full_name, books.price, books.stock_quantity
                FROM books
                JOIN genres ON books.genre_id = genres.id
                JOIN authors ON books.author_id = authors.id
                ORDER BY books.stock_quantity ASC"""
        try:
            with DatabaseConnection() as db:
                books = db.execute_query(query)
                
                # Prepare the data for tabulation
                headers = ["ID", "Book Title", "Genre", "Author", "Price $", "Stock"]  # Table headers
                # Process each book row
                book_data = [(book[0], book[1], book[2], book[3], book[4], book[5]) for book in books]

                # Use tabulate to format and print the table
                print(tabulate.tabulate(book_data, headers=headers, tablefmt="pretty"))
        
        except Exception as e:
            print(f"Error listing books: {e}")
        
    # def listLowStockBooks():

            