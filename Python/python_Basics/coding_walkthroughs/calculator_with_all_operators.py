# Basic calc (googled)

# Welcome greeting
def welcome():
    print("Welcome to the calculator!\n")
welcome()

# Making functions for the calculator:
def calc():
    print("Please choose an operation: \n"
          "1. Add\n"
          "2. Subtract\n"
          "3. Multiply\n"
          "4. Divide\n"
          "5. Power\n"
          "6. Modulo\n")
    # Take input from the user
    choice = int(input("Enter 1, 2, 3, 4, 5 or 6: "))
    num1 = int(input("Input your first number: "))
    num2 = int(input("Input your second number: "))

    # Function for addition
    def add(num1, num2):
        return num1 + num2

    # Function for subtraction
    def subtract(num1, num2):
        return num1 - num2

    # Function for multiplication
    def multiply(num1, num2):
        return num1 * num2

    # Function for division
    def divide(num1, num2):
        return num1 / num2
    # Function for power
    def power(num1, num2):
        return num1 ** num2

    # Function for modulo (finding a remainder):
    def modulo(num1, num2):
        return num1 % num2

    if choice == 1:
        print(num1, '+', num2, '=', add(num1, num2))
    elif choice == 2:
        print(num1, '-', num2, '=', subtract(num1, num2))
    elif choice == 3:
        print(num1, 'x', num2, '=', multiply(num1, num2))
    elif choice == 4:
        print(num1, '/', num2, '=', divide(num1, num2))
    elif choice == 5:
        print(num1, '^', num2, "=", power(num1, num2))
    elif choice == 6:
        print(num1, '%', num2, '=', modulo(num1, num2))
    else:
        print('Invalid input :(')

calc()

def another():
    calc_active = True
    while calc_active:
        again = input("\nWould you like to calculate again? "
                  "\nType y for Yes or n for No: ")
    # Take user's response
        if again == 'y':
            calc()
        elif again == 'n':
            print("\nSee you later!")
            calc_active = False

another()