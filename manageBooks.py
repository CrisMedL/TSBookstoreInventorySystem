from menu_system import show_manage_books_menu, clear_console_screen
from book import Book
from author import Author
from genre import Genre
import os

def manageBooks():
    while True:
        show_manage_books_menu()
        choice = input("Please select the number associated with the action you want to perform: ").strip()
        
        match choice:
            case "1":
                clear_console_screen()
                print("Adding a new book...")
                try:
                    book_title = input("Enter Book Title: ").strip().title()
                    if not book_title:
                        raise ValueError("Book title cannot be empty.")

                    Genre.listGenres
                    genre_id = int(input("Enter Genre ID: ").strip())
                    if genre_id <= 0:
                        raise ValueError("Genre ID must be a positive integer.")
                    
                    Author.listAuthors
                    author_id = int(input("Enter Author ID: ").strip())
                    if author_id <= 0:
                        raise ValueError("Author ID must be a positive integer.")

                    price = float(input("Enter Book Price: ").strip())
                    if price < 0:
                        raise ValueError("Price cannot be negative.")

                    stock_quantity = int(input("Enter Stock Quantity: ").strip())
                    if stock_quantity < 0:
                        raise ValueError("Stock quantity cannot be negative.")

                    book = Book(
                        book_title=book_title,
                        genre_id=genre_id,
                        author_id=author_id,
                        price=price,
                        stock_quantity=stock_quantity
                    )
                    book.addBook()
                except ValueError as ve:
                    print(f"Input Error: {ve}")
                except Exception as e:
                    print(f"Unexpected Error: {e}")

            case "2":
                clear_console_screen()
                print("Updating an existing book...")
                try:
                    book_id = int(input("Enter Book ID to update: ").strip())
                    if book_id <= 0:
                        raise ValueError("Book ID must be a positive integer.")

                    book_title = input("Enter New Book Title: ").strip().title()
                    genre_id = int(input("Enter New Genre ID: ").strip())
                    author_id = int(input("Enter New Author ID: ").strip())
                    price = float(input("Enter New Price: ").strip())
                    stock_quantity = int(input("Enter New Stock Quantity: ").strip())

                    book = Book(
                        book_id=book_id,
                        book_title=book_title,
                        genre_id=genre_id,
                        author_id=author_id,
                        price=price,
                        stock_quantity=stock_quantity
                    )
                    book.updateBook()
                except ValueError as ve:
                    print(f"Input Error: {ve}")
                except Exception as e:
                    print(f"Unexpected Error: {e}")

            case "3":
                clear_console_screen()
                print("Deleting a book...")
                try:
                    book_id = int(input("Enter Book ID to delete: ").strip())
                    if book_id <= 0:
                        raise ValueError("Book ID must be a positive integer.")
                    
                    book = Book(book_id=book_id)
                    book.deleteBook()
                except ValueError as ve:
                    print(f"Input Error: {ve}")
                except Exception as e:
                    print(f"Unexpected Error: {e}")

            case "4":
                clear_console_screen()
                print("Listing by Identifier")
                try:
                    Book.sortBooksByIdentifier()
                except Exception as e:
                    print(f"Error listing books: {e}")

            case "5":
                clear_console_screen()
                print("Listing by Title")
                try:
                    Book.sortBooksByTitle()
                except Exception as e:
                    print(f"Error listing books: {e}")

            case "6":
                clear_console_screen()
                print("Listing by Author")
                try:
                    Book.sortBooksByAuthor()
                except Exception as e:
                    print(f"Error listing books: {e}")

            case "7":
                clear_console_screen()
                print("Listing by Stock")
                try:
                    Book.sortBooksByStock()
                except Exception as e:
                    print(f"Error listing books: {e}")

            case "8":
                clear_console_screen()
                print("Listing by Price")
                try:
                    Book.sortBooksByPrice()
                except Exception as e:
                    print(f"Error listing books: {e}")

            case "0":
                print("Returning to main menu...")
                clear_console_screen()
                break

            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    manageBooks()
