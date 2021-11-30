# functions

# DRY -> "Don't Repeat Yourself"
def print_item():
    print("example")
print_item()

def full_name(first_name, last_name):
    return first_name + ' ' + last_name

def print_name(data_type):
    print(data_type)

print_name(full_name("ebony", "gordon"))