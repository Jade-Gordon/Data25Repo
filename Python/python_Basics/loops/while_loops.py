# While loop = a statement that'll execute it's block of code,
#               as long as it's condition remains true

# # loop_control = True
# counter = 0
# while counter < 10:
#     if counter % 2 == 0:
#         print(counter)   # if counter is divisible by 2
#     else:
#         print("odd number")
#     counter += 1

name = "" # Can also be name = None

while len(name) == 0: # while not name:
    name = input("Enter your name: ")

print("Hello " + name)
# If I keep ignoring the prompt to enter my name (by clicking enter)
# the while loop condition is true as the length of name is 0
# As my name has a length of 4 (!=0), the while loop condition is now false

