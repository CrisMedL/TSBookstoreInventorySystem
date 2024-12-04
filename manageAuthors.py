from author import Author
from messages_and_menus import show_manage_authors_menu
import os

def manageAuthors():
    # Function to display options for managing authors and handle user input.
    while True:
        show_manage_authors_menu()
        choice = input("Please select the number associated with the action you want to perform: ").strip()

        match choice:
            case "1":
                print("Adding a new author...")
                while True:  # Loop for valid author name input
                    try:
                        author_full_name = input("Enter author's full name: ").strip().upper()
                        if not author_full_name:
                            raise ValueError("Author's name cannot be empty.")
                        # Here you could also add further checks like not allowing numbers, etc.
                        author = Author(author_full_name)  
                        author.addAuthor()
                        break  # Exit loop when adding is successful
                    except ValueError as e:
                        print(e)

            case "2":
                Author.listAuthors()  # List authors before asking for an ID to update
                print("Updating an existing author...")
                while True:  # Loop for valid author ID input
                    try:
                        author_id = int(input("Enter the ID of the author to update: ").strip())
                        if author_id <= 0:
                            raise ValueError("ID must be a positive integer.")
                        author_full_name = input("Enter updated author's name: ").strip().capitalize()
                        if not author_full_name:
                            raise ValueError("Author's name cannot be empty.")
                        author = Author(author_id, author_full_name)  
                        author.updateAuthor()
                        break  # Exit loop when update is successful
                    except ValueError as e:
                        print(f"Invalid input: {e}")

            case "3":
                print("Deleting an author...")
                Author.listAuthors()
                while True:  # Loop for valid author ID input
                    try:
                        author_id = int(input("Enter the ID of the author to delete: ").strip())
                        if author_id <= 0:
                            raise ValueError("ID must be a positive integer.")
                        author = Author(author_id=author_id)  
                        author.deleteAuthor()
                        break  # Exit loop when deletion is successful
                    except ValueError as e:
                        print(f"Invalid input: {e}")

            case "4":
                print("Listing all authors...")
                try:
                    Author.listAuthors()
                except Exception as e:
                    print(f"Error: {e}")
                break
            case "0":
                print("Returning to main menu...")
                os.system('cls' if os.name == 'nt' else 'clear')  # Clear console screen
                break

            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    manageAuthors()
