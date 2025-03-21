from menu_system import *
from book import Book
from author import Author
from genre import Genre
from manageGenres import *
from manageAuthors import * 
import os



def manageBooks():
    while True:
        show_manage_books_menu()
        choice = input("Please select the number associated with the action you want to perform: ").strip()
        match choice:
            case "1": 
                while True:
                    clear_console_screen()
                    print("Adding a new book...")

                    try:
                        book_title = input("Enter Book Title: ").title().strip()
                        if not book_title:
                            raise ValueError("Book title cannot be empty.")

                        Genre.listGenres()
                        while True:
                            try:
                                genre_name = input("Enter Genre name: ").title().strip()
                                genre = Genre(genre_name=genre_name)
                                if not genre.checkGenreExistsByName(): 
                                    print("Genre not found! Please add it to the database to proceed.")
                                    time.sleep(1.5)
                                    clear_console_screen()
                                    add_genre_prompt()
                                    genre_id = genre.fetchGenreId()
                                    break                                      
                                else:
                                    genre_id = genre.fetchGenreId()
                                    break
                            except Exception:
                                print("Invalid input. Please enter a valid genre name.")

                        Author.listAuthors()
                        while True:
                            try:
                                author_name = input("Now select an author: ").title().strip()
                                author = Author(author_full_name=author_name)
                                if not author.checkAuthorExists():  
                                    print("Author not found! Please add it to the database and then pick the appropriate author")
                                    time.sleep(1.5)
                                    clear_console_screen()
                                    add_author_prompt()
                                    author_id = author.fetchAuthorId()
                                    break  
                                else:
                                    author_id = genre.fetchGenreId()
                                    break

                            except ValueError:
                                print("Invalid input. Please enter a valid integer.")

                        while True:
                            try:
                                price = float(input("Enter Book Price: ").strip())
                                if price < 0:
                                    print("Price cannot be negative. Please try again.")
                                else:
                                    break
                            except ValueError:
                                print("Invalid input. Please enter a valid number for the price.")

                        while True:
                            try:
                                stock_quantity = int(input("Enter Stock Quantity: ").strip())
                                if stock_quantity < 0:
                                    print("Stock quantity cannot be negative. Please try again.")
                                else:
                                    break
                            except ValueError:
                                print("Invalid input. Please enter a valid integer for the stock quantity.")

                        # Create and add the book
                        book = Book(book_title=book_title, genre_id=genre_id, author_id=author_id, price=price, stock_quantity=stock_quantity)
                        book.addBook()
                        print("Book added successfully!")

                        add_another = input("Do you want to add another book? (yes/no): ").strip().lower()
                        if add_another != 'yes':
                            break  # Exit the loop and return to the main menu
                    except ValueError as ve:
                        print(f"Input Error: {ve}")
                    except Exception as e:
                        print(f"Unexpected Error: {e}")

                    input("Press Enter to try again...")


            case "2":  
                clear_console_screen()
                print("Updating an existing book...")
                Book.listBooksByIdentifier()
                try:
                    book_id = int(input("Enter Book ID to update: ").strip())
                    if book_id <= 0: 
                        raise ValueError("Book ID must be a positive integer.")
                    else:
                        clear_console_screen()
                        print(f"Currently modifying the following book:")
                        book = Book(book_id=book_id)  
                        book.fetchSingleBook() # Fetch and display book details

                        show_update_books_menu()
                        update_choice = input("Please select the number associated with the action you want to perform: ").strip()
                        match update_choice:
                            case "1":  # Update book title
                                clear_console_screen()
                                print(f"Currently modifying book title of book:")
                                book.fetchSingleBook()
                                new_title = input("Enter new Book Title: ").strip().title()
                                if not new_title:
                                    raise ValueError("Book title cannot be empty.")
                                else:
                                    book = Book(book_id=book_id, book_title=new_title)
                                    book.updateBookTitle()
                                    print("Book title updated successfully!")
                            case "2":  # Update genre
                                clear_console_screen()
                                Genre.listGenres()
                                new_genre_id = int(input("Enter new Genre ID for this book: ").strip())
                                if new_genre_id <= 0:
                                    raise ValueError("Genre ID must be a positive integer.")
                                else:
                                    book = Book(book_id=book_id, genre_id=new_genre_id)
                                    book.updateBookGenre()
                                    print("Genre updated successfully!")
                            case "3":  # Update author
                                clear_console_screen()
                                Author.listAuthors()
                                new_author_id = int(input("Enter new Author ID: ").strip())
                                if new_author_id <= 0:
                                    raise ValueError("Author ID must be a positive integer.")
                                else:
                                    book = Book(book_id=book_id, author_id=new_author_id)
                                    book.updateBookAuthor()
                                    print("Author updated successfully!")
                            case "4":  # Update price
                                clear_console_screen()
                                Book.fetchSingleBook(book_id=book_id)
                                new_price = float(input("Enter new Book Price: ").strip())
                                if new_price < 0:
                                    raise ValueError("Price cannot be negative.")
                                else:
                                    book = Book(book_id=book_id, price=new_price)
                                    book.updateBookPrice()
                                    print("Price updated successfully!")
                            case "5":  # Update stock quantity
                                clear_console_screen()
                                Book.fetchSingleBook(book_id=book_id)
                                new_stock_quantity = int(input("Enter new Stock Quantity: ").strip())
                                if new_stock_quantity < 0:
                                    raise ValueError("Stock quantity cannot be negative.")
                                else:
                                    book = Book(book_id=book_id, stock_quantity=new_stock_quantity)
                                    book.updateBookStock()
                                    print("Stock quantity updated successfully!")
                            case "0":
                                clear_console_screen()
                                break
                            case _:  # Handle invalid choices
                                print("Invalid choice. Please try again.")
                except ValueError as ve:
                    print(f"Input Error: {ve}")
                except Exception as e:
                    print(f"Unexpected Error: {e}")

            
            case "3": 
                clear_console_screen()
                print("Deleting a book...")
                Book.listBooksByIdentifier()  
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

            case "4": #Option 4
                clear_console_screen()
                print("Listing by Identifier")
                try:
                    Book.listBooksByIdentifier()
                except Exception as e:
                    print(f"Error listing books: {e}")

            case "5": # Option 5
                clear_console_screen()
                print("Listing by Title")
                try:
                    Book.listBooksByTitle()
                except Exception as e:
                    print(f"Error listing books: {e}")

            case "6": # Option 6
                clear_console_screen()
                print("Listing by Author")
                try:
                    Book.listBooksByAuthor()
                except Exception as e:
                    print(f"Error listing books: {e}")

            case "7": 
                clear_console_screen()
                print("Listing by Stock")
                try:
                    Book.listBooksByStock()
                except Exception as e:
                    print(f"Error listing books: {e}")

            case "8": 
                clear_console_screen()
                print("Listing by Price")
                try:
                    Book.listBooksByPrice()
                except Exception as e:
                    print(f"Error listing books: {e}")
            
            case "9":
                clear_console_screen()
                print("Listing low stock books:")
                try:
                    Book.listLowStockBooks()
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