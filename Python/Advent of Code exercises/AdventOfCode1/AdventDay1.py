# 5 years in a row
# cash only, own currency
# find 50 stars
# find 50 coins by
# each puzzle grants one star
#expense report
# find 2 numbers (entries) that sum up 2020
# then multiply them together
# there are 200 inputs
# e.g. two entries that sum up to 2020 are 1721+299

# import nums from txt file into this file

# then create func to find nums that match (sum up to 2020)
# use a for loop to:
# then multiply those nums together
# import numpy as np
# filename = "expense_report.txt"
# data = np.loadtxt(filename, delimiter=',')

list1 = []
with open("expense_report.txt", newline='') as expense_report_file:
    # expense_report = expense_report_file.readlines()
    for row in expense_report_file:
        list1.append(int(row))

# Find two numbers that add together:
def add_two_nums(list):
    for x in list:
        for y in list:
            if x != y and x + y == 2020:
                print(f"Found them! They are: {x} + {y}")
                return x * y

print(add_two_nums(list1))

# part 2 -> find 3 numbers
def add_three_nums(list1):
    for x in list1:
        for y in list1:
            for z in list1:
                if x != y and y != z and x + y + z == 2020:
                    print(f"Found them! They are: {x} + {y} + {z}")
                    return x * y * z

print(add_three_nums(list1))
# def add_two_nums(expense):
#    try:
#         with open(expense, "r") as expense_report:
#             file_line_list = expense_report.readlines()
#         for line in file_line_list:
#             print(line.replace("\n", ""))
#
#    except FileNotFoundError as errmsg:
#        print("There's no file...PANIC!", errmsg)
#         # for x in expense:
#         # for y in expense_report:
#         # if x + y == 2020
#         #     return x, y
#     #for num2 in
# #add_two_nums()
#    finally:
#         print("Execution complete!")
# add_two_nums("expense_report.txt")
