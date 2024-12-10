from author import Author
from menu_system import show_manage_authors_menu, clear_console_screen


def add_author_prompt():
    clear_console_screen()
    print("Adding a new author...")
    while True:  # Loop for valid author name input
        try:
            Author.listAuthors()
            author_full_name = input("Enter author's full name (or 'x' to cancel): ").strip()
            
            if author_full_name.lower() == 'x':
                print("Exiting the add author option...")
                return  # Exit the function to return to the previous menu
            
            if not author_full_name:
                raise ValueError("Author's name cannot be empty.")
            else:
                author_full_name = author_full_name.capitalize()  # Capitalize only the first letter of the string
                author = Author(author_full_name=author_full_name)
                author.addAuthor()
                print(f"Author '{author_full_name}' has been added successfully.")
                break  # Exit loop when addition is successful
        
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
            author_id = input("Enter the ID of the author to update (or 'x' to cancel): ").strip().lower()
            
            if author_id == 'x':
                print("Exiting the update author option...")
                return  # Exit the function to return to the previous menu
            
            if not author_id.isdigit() or int(author_id) <= 0:
                raise ValueError("ID must be a positive integer.")
            
            author_id = int(author_id)
            author = Author(author_id=author_id)
            
            if not author.checkAuthorExists():
                print("Author does not exist. Please try again.")
            else:
                author_full_name = input("Enter updated author's name (or 'x' to cancel): ").strip()
                
                if author_full_name.lower() == 'x':
                    print("Exiting the update author option...")
                    return  # Exit the function to return to the previous menu
                
                if not author_full_name:
                    raise ValueError("Author's name cannot be empty.")
                
                author_full_name = author_full_name.title()  # Capitalize the first letter of each word
                author = Author(author_id=author_id, author_full_name=author_full_name)
                author.updateAuthor()
                print(f"Author with ID {author_id} has been updated to '{author_full_name}'.")
                break  # Exit loop when update is successful
        
        except ValueError as e:
            print(f"Invalid input: {e}")
        except Exception as e:
            print(f"Unexpected Error: {e}")
            break


def delete_author_prompt():
    clear_console_screen()
    print("Deleting an author...")
    Author.listAuthors()  # List authors before allowing the user to select one
    while True:  # Loop for valid author ID input
        try:
            author_id_input = input("Enter the ID of the author to delete (or 'x' to cancel): ").strip()

            if author_id_input.lower() == 'x':
                print("Exiting the delete author option...")
                return  # Exit the function to return to the previous menu

            author_id = int(author_id_input)  # Convert the stripped input to an integer
            if author_id <= 0:
                raise ValueError("ID must be a positive integer.")

            author = Author(author_id=author_id)

            # Check if the author exists in the database
            if not author.checkAuthorExists():
                print("Author does not exist in the database. Cannot delete it.")
                break  # Exit the loop if author does not exist
            else:
                author.deleteAuthor()  # Delete the author if it exists
                print(f"Author with ID {author_id} has been deleted successfully.")
                break  # Exit loop when deletion is successful
        except ValueError as e:
            print(f"Invalid input: {e}")
        except Exception as e:
            print(f"Unexpected Error: {e}")
            break


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

if __name__ == "__main__":
    manageAuthors()