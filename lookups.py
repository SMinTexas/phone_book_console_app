# All lookup functionality contained here
import book
import menu
import results

from globals import list_of_names, list_of_phone_numbers

# By name
def get_phone_by_name(search_str):
    for i in list_of_names:
        if i == search_str:
            index = list_of_names.index(i)
            phoneno = list_of_phone_numbers[index]
            print(results.result_by_name(search_str, phoneno))
            menu.blank_line()

def get_name_by_phone(search_str):
    for i in list_of_phone_numbers:
        if i == search_str:
            index = list_of_phone_numbers.index(i)
            name = list_of_names[index]
            print(results.result_by_phone(search_str, name))
            menu.blank_line()




