# # # Errors
# #
# number = int(input("Enter a number: "))
# # Converting the input into an integer
# print(number)
# # If I enter "8" no error occurs
# # If I enter "eight" I get a "ValueError"

#try except block
# this helps protect our code from an error
#we can accept SPECIFIC errors
try:
    answer = 10/0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)
except ValueError:
    print("Invalid Input")

# we can also store the ZeroDivisionError as an input
#
# i = 1
# while i < 6:
#     print(i)
#     i += 1