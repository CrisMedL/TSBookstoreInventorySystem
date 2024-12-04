from menu_system import show_manage_genres_menu, clear_console_screen
import os
from genre import Genre

def manageGenres():
    # Function to display options for managing genres and handle user input.
    while True:
        show_manage_genres_menu()
        choice = input("Please select the number associated with the action you want to perform: ").strip()
        match choice:
            case "1":
                clear_console_screen()
                print("Adding a new genre...")
                while True:  # Loop for valid genre name input
                    try:
                        Genre.listGenres()
                        genre_name = input("Enter Genre Name: ").strip().capitalize()
                        if not genre_name:
                            raise ValueError("Genre name cannot be empty.")
                        genre = Genre(genre_name=genre_name)
                        genre.addGenre()
                        break
                    except ValueError as e:
                        print(f"Input Error: {e}")
                    except Exception as e:
                        print(f"Unexpected Error: {e}")
                        break

            case "2":
                clear_console_screen()
                print("Updating an existing genre...")
                try:
                    Genre.listGenres()  # List genres before allowing the user to select one
                except Exception as e:
                    print(f"Error listing genres: {e}")
                    break
                
                while True:  # Loop for valid genre ID input
                    try:
                        genre_id_input = input("Enter the ID of the genre to update: ").strip()
                        genre_id = int(genre_id_input)  # Convert the stripped input to an integer
                        if genre_id <= 0:
                            raise ValueError("ID must be a positive integer.")
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

            case "3":
                clear_console_screen()
                print("Deleting a genre...")
                try:
                    Genre.listGenres()  # List genres before allowing the user to select one
                except Exception as e:
                    print(f"Error listing genres: {e}")
                    continue

                while True:  # Loop for valid genre ID input
                    try:
                        genre_id_input = input("Enter the ID of the genre to delete: ").strip()
                        genre_id = int(genre_id_input)  # Convert the stripped input to an integer
                        if genre_id <= 0:
                            raise ValueError("ID must be a positive integer.")
                        genre = Genre(genre_id=genre_id)
                        genre.deleteGenre()
                        break  # Exit loop when deletion is successful
                    except ValueError as e:
                        print(f"Input Error: {e}")
                    except Exception as e:
                        print(f"Unexpected Error: {e}")
                        break

            case "4":
                clear_console_screen()
                print("Listing all genres...")
                try:
                    Genre.listGenres()
                except Exception as e:
                    print(f"Error: {e}")
                break

            case "0":
                print("Returning to main menu...")
                os.system('cls' if os.name == 'nt' else 'clear')  # Clear console screen
                break

            case _:
                print("Invalid choice. Please try again.")

