# String concatenation and escape characters

first_name = 'jane'
last_name = 'doe'
full_name = first_name + ' ' + last_name
age = 25
# You can't add a string to an integer...
# ...you can't print full_name (str) + age (int)
print(full_name + ' ' + str(age))

# escape characters -> \"___\"
text = "someone then said, \"text can be trick\""
# The same works for single quotation marks -> ''
print(text)