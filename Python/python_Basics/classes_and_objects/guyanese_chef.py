#Let's say that the Guyanese Chef can do
# everything the normal chef can do
from chef import Chef
# inherit: make Chef the argument in GuyaneseChef func
class GuyaneseChef(Chef):
    def make_special_dish(self):
        # override normal chef's special dish
        print("The chef makes curried mutton")

    def make_roti(self):
        print("The chef makes roti")