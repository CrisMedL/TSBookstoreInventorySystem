from messages_and_menus import show_manage_genres_menu
import os
from genre import Genre

def manageGenres():
    # Function to display options for managing genres and handle user input.
    while True:
        show_manage_genres_menu()
        choice = input("Please select the number associated with the action you want to perform: ").strip()
        match choice:
            case "1":
                print("Adding a new genre...")
                genre_name = input("Enter Genre Name: ").strip().capitalize()
                if not genre_name:
                    print("Genre name cannot be empty.")
                    continue
                genre = Genre(genre_name=genre_name)
                try:
                    genre.addGenre()
                except Exception as e:
                    print(f"Error: {e}")
            case "2":
                print("Updating an existing genre...")
                Genre.listGenres()  # List genres before allowing the user to select one
                genre_id = int(input("Enter the ID of the genre to update: ")).strip()
                if genre_id <= 0:
                        raise ValueError("ID must be a positive integer.")
                genre_name = input("Enter New Genre Name: ").strip().capitalize()

                if not genre_name:
                    print("Genre name cannot be empty.")
                    continue
                genre = Genre(genre_id=genre_id, genre_name=genre_name)
                try:
                    genre.updateGenre()
                except Exception as e:
                    print(f"Error: {e}")
            case "3":
                print("Deleting a genre...")
                Genre.listGenres()  # List genres before allowing the user to select one
                genre_id = int(input("Enter the ID of the genre to delete: ")).strip()
                if genre_id <= 0:
                    raise ValueError("ID must be a positive integer.")
                genre = Genre(genre_id=genre_id)
                try:
                    genre.deleteGenre()
                except Exception as e:
                    print(f"Error: {e}")
            case "4":
                print("Listing all genres...")
                try:
                    Genre.listGenres()
                except Exception as e:
                    print(f"Error: {e}")
            case "0":
                print("Returning to main menu...")
                os.system('cls' if os.name == 'nt' else 'clear')  # Clear console screen
                break
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    manageGenres()
