# This controls the prompts the user sees
import menu

def select_option():
    user_choice = input("What do you want to do (1-5)? ")
    menu.blank_line()
    return user_choice

def print_prompt(selection):
    if selection == 1:
        return "By name or by phone number (Enter N or P)? "
    elif selection == 3:
        return "Name: "
    elif selection == 5:
        return "Auf Wiedersehen"
    elif selection < 1 or selection > 5:
        return "Please select a value between 1 and 5"

# Prompt for looking up an entry by name or phone number
def print_subprompt(selection, style):
    if (selection == 1 and style == "N"):
        return "Name: "
    elif (selection == 1 and style == "P"):
        return "Phone Number: "

# Prompt for adding a new entry name
def print_add_name_prompt():
    return "Name: "

# Prompt for adding a new entry phone number
def print_add_phone_prompt():
    return "Phone Number: "
