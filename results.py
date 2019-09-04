# This is for the results of the requested operations

# Looking up by name
def result_by_name(name, phone):
    return name + " can be reached at " + phone

# Looking up by phone
def result_by_phone(phone, name):
    return "Phone number " + phone + " belongs to " + name

# Add a new entry
def result_by_add(name):
    return "Entry stored for " + name

# Delete an existing entry
def result_by_delete(name):
    return "Deleted entry for " + name

# Display the list
def result_by_full(name, phone):
    return "Entry found for " + name + " " + phone