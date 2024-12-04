from menu_system import *
from manageAuthors import manageAuthors
from manageGenres import manageGenres
from manageBooks import manageBooks


# Function to run the program
def run_program():
    show_opening_message()
    menu()

def clear_console_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Main menu function (for later calling)
def menu():
    while True:
        show_main_menu()
        choice = input("Enter your choice: ").strip()
        match choice:
            case "1":
                clear_console_screen()
                manageGenres()
            case "2":
                clear_console_screen()
                manageAuthors()
            case "3":   
                clear_console_screen()
                manageBooks()
            case "0":
                clear_console_screen()
                message = ("Saving data...\n"
                           "Data saved successfully!\n"
                           "Closing program...\n")
                typewriter_message(message)
                break
            case _:
                print("Invalid choice. Please try again.")

