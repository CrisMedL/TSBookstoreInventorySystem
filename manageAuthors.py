from author import Author
from menu_system import show_manage_authors_menu, clear_console_screen
import os


def add_author_prompt():
    clear_console_screen()
    print("Adding a new author...")
    while True:  # Loop for valid author name input
        try:
            Author.listAuthors()
            author_full_name = input("Enter author's full name: ").strip().capitalize()
            if not author_full_name:
                raise ValueError("Author's name cannot be empty.")
            else:
                author = Author(author_full_name=author_full_name)  
                author.addAuthor()
                break
        except ValueError as e:
            print(f"Input Error: {e}")
        except Exception as e:
            print(f"Unexpected Error: {e}")
            break

def update_author_prompt():
    clear_console_screen()  # List authors before asking for an ID to update
    print("Updating an existing author...")

    try:
        Author.listAuthors()
    except Exception as e:
        print(f"Error listing authors: {e}")

    while True:  # Loop for valid author ID input
        try:
            author_id = int(input("Enter the ID of the author to update: "))
            if author_id <= 0:
                raise ValueError("ID must be a positive integer.")
            author = Author(author_id=author_id)
            if not author.checkAuthorExists():
                break
            else:
                author_full_name = input("Enter updated author's name: ").strip().title()
                if not author_full_name:
                    raise ValueError("Author's name cannot be empty.")
                author = Author(author_id, author_full_name)  
                author.updateAuthor()
                break
        except ValueError as e:
            print(f"Invalid input: {e}")
        except Exception as e:
            print(f"Unexpected Error: {e}")
            break

def delete_author_prompt():
    clear_console_screen()
    print("Deleting an author...")
    Author.listAuthors()
    while True:  # Loop for valid author ID input
        try:
            author_id = int(input("Enter the ID of the author to delete: "))
            if author_id <= 0:
                raise ValueError("ID must be a positive integer.")
            author = Author(author_id=author_id)
            if not author.checkAuthorExists(): 
                print("Author does not exists in database. Cannot delete it.")
                break
            else:
                author.deleteAuthor()
                break
        except Exception:
            print("Something went wrong...Taking you back to the menu")
            break  # Stop after an unexpected error

def list_authors_prompt():
    clear_console_screen()
    print("Listing all authors...")
    try:
        Author.listAuthors()
    except Exception as e:
        print(f"Error: {e}")

def manageAuthors():
    # Function to display options for managing authors and handle user input.
    while True:
        show_manage_authors_menu()
        choice = input("Please select the number associated with the action you want to perform: ").strip()

        match choice:
            case "1":
                add_author_prompt()
            case "2":
                update_author_prompt()
            case "3":
                delete_author_prompt()
            case "4":
                list_authors_prompt()
            case "0":
                print("Returning to main menu...")
                clear_console_screen()
                break

            case _:
                print("Invalid choice. Please try again.")

