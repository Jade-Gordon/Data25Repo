# Reading from files outside py
# using the python read command
# I don't have a txt file readily available :|
"""
Have the file you want to read and write in
 in the same directory as the Python file
 you're coding in!
Modes:
"r" = read
"w" = write
"a" = append
"r+" = read and write
"""
# open the file...set as a var
# employee_file = open("file.txt", "r")
# # check that it's readable
# # print(employee_file.readable())
# # read the file
# print(employee_file.read())
# #read a line in the file
# print(employee_file.readline())
# # read lines in the file, which then prints out a list
# print(employee_file.readlines())
# employee_file = open("employee.txt", "r")
# for employee in employee_file.readlines():
#     print(employee)
# # close the file. Always do this at the end.
# It's good practise
# employee_file.close()


# Writing files
# # I want to add text to the end of the file:
# employee_file = open("employees.txt", "a")
# employee_file.write("Huey - HR")
# # Be careful when appending files
# # If you accidentally run the code again,
# # The text won't go to the next line
# # add a new line -> \n
# employee_file.write("\nKate - Customer Services")
# employee_file.close()
# # "w" overwrites the existing file! Hence "a" is used to added elements
# # We can use "w" to create a new file
# employee_file1 = open("employee1.txt", "w")
# employee_file1.close()


