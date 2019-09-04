# You will write a command line program to manage a phone book. 
# When you start the phonebook.py program, it will print out a menu 
# and ask the user to enter a choice:

# $ python3 phonebook.py 
# Electronic Phone Book 
# ===================== 
# 1. Look up an entry 
# 2. Set an entry 
# 3. Delete an entry 
# 4. List all entries 
# 5. Quit
# What do you want to do (1-5)?

# 1. If they choose to look up an entry, you will ask them for the person's name, and then look up the person's phone number by the given name and print it to the screen.
# 2. If they choose to set an entry, you will prompt them for the person's name and the person's phone number,
# 3. If they choose to delete an entry, you will prompt them for the person's name and delete the given person's entry.
# 4. If they choose to list all entries, you will go through all entries in the dictionary and print each out to the terminal.
# 5. If they choose to quit, end the program.

import book
import menu
import lookups
import adds
import deletes
import display_list
import options

menu.print_menu()
menu_choice = 0

while menu_choice != 5:
    menu_choice = int(options.select_option())

    if menu_choice == 1:
        option = input(options.print_prompt(menu_choice))
        if option == "N":
            name = input(options.print_subprompt(menu_choice, option))
            print(name)
            lookups.get_phone_by_name(name)
        elif option == "P":
            phone = input(options.print_subprompt(menu_choice, option))
            lookups.get_name_by_phone(phone)
    elif menu_choice == 2:
        name = input(options.print_add_name_prompt())
        phone = input(options.print_add_phone_prompt())
        adds.add_new_entry(name, phone)
    elif menu_choice == 3:
        name = input(options.print_prompt(menu_choice))
        deletes.del_entry(name)
    elif menu_choice == 4:
        display_list.print_entries()
    elif menu_choice == 5:
        print(options.print_prompt(menu_choice))
    else:
        print(options.print_prompt(menu_choice))

