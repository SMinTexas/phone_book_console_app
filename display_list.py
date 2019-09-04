# All code to display the phone book will go here
import book
import menu
import results

def print_entries():
    length_of_list = len(book.phonebook)   
    for x in range(0, length_of_list):
        name = book.phonebook[x]['name']
        phone = book.phonebook[x]['phone']
        print(results.result_by_full(name, phone))
        
    menu.blank_line()