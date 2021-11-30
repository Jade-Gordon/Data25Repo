# For loop
# dependent on iterables
# - it checks EVERY ITEM in that object!
# That includes dicts and lists

# when considering iterables: do they hold >1 data type?

# example_string = "test"

# It makes sense to call the variable "character" cos each character in the string will be cycled through
# for character in example_string:
  #   print(character)

# for loop =    a statement that'll execute it's block of code
#               a limited amount of times

#               while loop = unlimited
#               for loop = limited

basket = ["eggs", "rice"]
for basket_item in basket:
    print(basket_item)

# Creating a dictionary with customers
customers = {
    "name": "Jade",
    "age": 22
}
for customer in customers.values():
    print(customer)
