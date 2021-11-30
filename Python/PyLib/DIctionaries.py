from pprint import pprint
dictionary_var = {"Jade": {"FavColour": "Teal", "LeastFav": "Pink"},
                  "Eden": ["Blue", "Purple"],
                  "Ensty": "Blue"}

print(dictionary_var.keys())
for i in dictionary_var.keys():
    print(dictionary_var[i])

# for i in dictionary_var.values():
# # reverse search
#     print(i)

print(dictionary_var["Eden"][1])
pprint(dictionary_var["Jade"]["LeastFav"])