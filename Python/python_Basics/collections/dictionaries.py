# Dictionary examples

# Key value pairs -> "key":"value"
# contact_list = {
 #  "jane": "07987755390"
# }
# contact_list["bob"] = "07844756001"
# print(contact_list["jane"])  # this gives the value of the key: the phone number
# print(contact_list.keys()) # returns the keys of the dictionary
# print(contact_list.values()) # returns the values in the dictionary

# Alphabetical contact list:
contact_list = {
    "a": {
        "anne": "07123456789"
    },
    "b": {
        "barry": "07855476501"
    },
    "c": {
        "connor": "07986435770"
    }
}
print(contact_list['b']['barry'])
# this gives barry's phone number, since we specifically called for it

# Quiz
theList = []
theList.append(1234)
theList.append(5678)
theList.append(99)
theList.append(5)
print(theList)
print(len(theList))     # the length of the list is 4...why? -> because it returns [1234, 5678, 99, 5]

"""
Main differences between lists and dicts:
1. The elements in a list are indexed with and int, whereas dict elements include their own key
2. The dict uses the key of each element to decide where to store the corresponding value
"""
