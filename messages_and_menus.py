# Native Python modules (no installation required)
import time  # For adding delays
import os  # For system-specific purposes (used to clear the console)
import sys # For interacting with the operating system 
import tabulate # For making pretty menus

# External Python libraries (must be installed via pip)
import pyfiglet  # For generating ASCII art
from termcolor import colored  # For adding colors to the ASCII art


def typewriter_message(message):
    
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char != "\n":
            time.sleep(0.05)
        else:
            time.sleep(1.5)
    time.sleep(2)

def show_opening_message():

    message= ("Initializing system...\n"
              "Doing some other things...\n"
              "Almost there...\n"
              "All good to go!\n")

    typewriter_message(message)

    os.system('cls' if os.name == 'nt' else 'clear') # Clear console screen

    # Generate the ASCII art text
    raw_text = pyfiglet.figlet_format("Welcome to\n C&L Bookstore", font="big", justify="center")

    # Add color to the text
    formatted_text = colored(raw_text, color="red")

    # Print the colored ASCII art text
    print(formatted_text)    
    time.sleep(4)  # For effect purposes

    os.system('cls' if os.name == 'nt' else 'clear')

def show_main_menu():
    menu_data = [
            ["1", "Manage Genres"],
            ["2", "Manage Authors"],
            ["3", "Manage Books"],
            ["0", "Exit"]
        ]
        # Format the menu using tabulate
    menu_table = tabulate.tabulate(menu_data, headers=["Option", "Description"], 
                                   tablefmt="pretty",
                                   numalign="center",
                                   stralign="center",
                                   colalign=("center","center"))
    print("\nBookstore Inventory Menu:")
    print(menu_table)

def show_manage_genres_menu():
    menu_data = [
        ["1", "Add Genre"],
        ["2", "Update Genre"],
        ["3", "Delete Genre"],
        ["4", "List Genres"],
        ["0", "Back"]
    ]

    menu_table = tabulate.tabulate(menu_data, headers=["Option", "Description"], 
                                   tablefmt="pretty",
                                   numalign="center",
                                   stralign="center",
                                   colalign=("center","center"))
    print(menu_table)

def show_manage_authors_menu():
    menu_data = [
        ["1", "Add Author"],
        ["2", "Update Author"],
        ["3", "Delete Author"],
        ["4", "List Authors"],
        ["0", "Back"]
    ]

    menu_table = tabulate.tabulate(menu_data, headers=["Option", "Description"], 
                                   tablefmt="pretty",
                                   numalign="center",
                                   stralign="center",
                                   colalign=("center","center"))
    print(menu_table)

def show_manage_books_menu():
    menu_data = [
        ["1", "Add Book"],
        ["2", "Update Book"],
        ["3", "Delete Book"],
        ["4", "Search Book"],
        ["5", "List Books by Identifier"],
        ["6", "List Books by Title"],
        ["7", "List Books by Author"],
        ["8", "List Books by Stock"],
        ["9", "List Books by Price"],
        ["0", "Back"]
    ]

    menu_table = tabulate.tabulate(menu_data, headers=["Option", "Description"], 
                                   tablefmt="pretty",
                                   numalign="center",
                                   stralign="center",
                                   colalign=("center","center"))
    print(menu_table)