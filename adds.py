# All add functionality contained here
import book
import menu
import results

def add_new_entry(name, phoneno):
    new_dict = {'name': name, 'phone': phoneno}
    book.phonebook.append(new_dict)
    print(results.result_by_add(name))
    menu.blank_line()