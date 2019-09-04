# All delete functionality goes here
import book
import menu
import results

def del_entry(name):
    # had to reset this from the global to prevent a crash on data that is not
    # included in the dataset.  Perhaps there is a different way to do this!
    list_of_names = [i["name"] for i in book.phonebook]

    index = list_of_names.index(name)
    del book.phonebook[index]
    print(results.result_by_delete(name))
    menu.blank_line()
