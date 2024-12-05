from menu_system import show_manage_genres_menu, clear_console_screen
import os
from genre import Genre


def add_genre_prompt():
    clear_console_screen()
    print("Adding a new genre...")
    while True:  # Loop for valid genre name input
        try:
            Genre.listGenres()
            genre_name = input("Enter Genre Name: ").strip().capitalize()
            if not genre_name:
                raise ValueError("Genre name cannot be empty.")
            else:
                genre = Genre(genre_name=genre_name)
                genre.addGenre()
                break
        except ValueError as e:
            print(f"Input Error: {e}")
        except Exception as e:
            print(f"Unexpected Error: {e}")
            break

def update_genre_prompt():
    clear_console_screen()
    print("Updating an existing genre...")
    try:
        Genre.listGenres()  # List genres before allowing the user to select one
    except Exception as e:
        print(f"Error listing genres: {e}")
    
    while True:  # Loop for valid genre ID input
        try:
            genre_id= int(input("Enter the ID of the genre to update: ").strip())# Convert the stripped input to an integer
            if genre_id <= 0:
                raise ValueError("ID must be a positive integer.")
            genre = Genre(genre_id=genre_id)
                                # Check if the genre exists in the database
            if not genre.checkGenreExistsById():
                break
            else:
                genre_name = input("Enter New Genre Name: ").strip().capitalize()
                if not genre_name:
                    raise ValueError("Genre name cannot be empty.")
                genre = Genre(genre_id=genre_id, genre_name=genre_name)
                genre.updateGenre()
                break  # Exit loop when updating is successful
        except ValueError as e:
            print(f"Input Error: {e}")
        except Exception as e:
            print(f"Unexpected Error: {e}")
            break
    
def delete_genre_prompt():
    clear_console_screen()
    print("Deleting a genre...")
    Genre.listGenres()  # List genres before allowing the user to select one
    while True:  # Loop for valid genre ID input
        try:
            genre_id = int(input("Enter the ID of the genre to delete: ").strip())  # Convert the stripped input to an integer
            if genre_id <= 0:
                raise ValueError("ID must be a positive integer.")
            genre = Genre(genre_id=genre_id)

            # Check if the genre exists in the database
            if not genre.checkGenreExistsById():
                print("Genre does not exist in the database. Cannot delete it.")
                break  # Exit the loop if genre does not exist
            else:
                genre.deleteGenre()  # Delete the genre if it exists
                break  # Exit loop when deletion is successful
        except ValueError as e:
            print(f"Invalid input: {e}")
        except Exception as e:
            print(f"Unexpected Error: {e}")
            break


def list_genres_prompt():
    clear_console_screen()
    print("Listing all genres...")
    try:
        Genre.listGenres()
    except Exception as e:
        print(f"Error: {e}")

def manageGenres():
    # Function to display options for managing genres and handle user input.
    while True:
        show_manage_genres_menu()
        choice = input("Please select the number associated with the action you want to perform: ").strip()
        match choice:
            case "1":
                add_genre_prompt()
            case "2":
                update_genre_prompt()
            case "3":
                delete_genre_prompt()
            case "4":
                list_genres_prompt()
            case "0":
                print("Returning to main menu...")
                os.system('cls' if os.name == 'nt' else 'clear')  # Clear console screen
                break

            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    manageGenres()