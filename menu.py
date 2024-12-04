from messages_and_menus import *
from manageAuthors import manageAuthors
from manageGenres import manageGenres
from manageBooks import manageBooks



def run_program():
    show_opening_message()
    menu()

def menu():
    while True:
        show_main_menu()
        choice = input("Enter your choice: ").strip()
        match choice:
            case "1":
                manageGenres()
            case "2":
                manageAuthors()
            case "3":   
                manageBooks()
            case "0":
                message = ("Saving data...\n"
                           "Data saved successfully!\n"
                           "Closing program...\n")
                typewriter_message(message)
                break
            case _:
                print("Invalid choice. Please try again.")

