# Lists (AKA arrays)
# can be a mix of data types

# example_list = [1, True, "string"] # single data types are ideal

shopping_list = ["eggs", "bread", "cheese"]
# shopping_list[1] = "apples"  # this replaces "bread" with "apples"
# shopping_list.append("mushrooms") # adds "mushrooms to the shopping list
# shopping_list.pop() # removes the last item from the list: "cheese"
# shopping_list.pop(0) # removes the first item from the list: "eggs"
print(shopping_list)
print(shopping_list.index("bread"))    # this gives the index of "bread": 1