"""
Booleans and equality operators

    Operator    |       Meaning              |       Example     |
        ==      |   equal to                 |   4 == 4 (True)   |
        !=      |   not equal to             |   4 != 3 (True)   |
        >       |   Greater than             |   3 > 4 (False)   |
        <       |   Less than                |   3 < 4 (True)    |
        >=      |   Greater than or equal to |   5 >= 5 (True)   |
        <=      |   Less than or equal to    |   5 <= 4 (False)  |
"""
# True or False
# print(type(True))
print(4 == 3) # returns "False"
print(2 < len("2")) # returns False because we only have 1 unicode character which is not equal to the int of 2

# Truthy or Falsey
print(bool(1)) # returns "True". This would be the same for all +ve and -ve intergers...
print(bool(0)) #...however, this returns "False"

print(bool("heyy"))     # returns "True"
print(bool(""))         # returns "False" since it's an empty string