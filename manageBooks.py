from messages_and_menus import show_manage_books_menu
from book import Book
import os

def manageBooks():
    while True:
        show_manage_books_menu()
        choice = input("Please select the number associated with the action you want to perform: ").strip()

        match choice:
            case "1":
                print("Adding a new book...")
                break
            case "2":
                print("Updating an existing book...")
                break
            case "3":
                print("Deleting a book...")
                break
            case "4":
                print("Listing and Sorting Books")
                try:
                    Book.listBooks()
                except Exception as e:
                    print(f"Error: {e}")
                break
            case "5":
                print("Discounts")
                break
            case "0":
                print("Returning to main menu...")
                os.system('cls' if os.name == 'nt' else 'clear')  # Clear console screen
                break
            case _:
                print("Invalid choice. Please try again.")





