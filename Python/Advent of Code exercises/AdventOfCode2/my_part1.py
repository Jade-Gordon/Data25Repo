import csv
# part 1
# eg valid password policy:   1-3 a: abcde
#                       the password must contain 1 <= "a" >= 3
# Q: How many passwords are valid?
def find_valid_one(csv_file_name):
    with open("advent_2.csv", newline="") as csv_file:
        find_passwords = csv.reader(csv_file, delimiter=" ")
# Need to find how many valid passwords there are:
        good_count = 0
    # Need to iterate through each line in the advent_2.csv file:
        for line in find_passwords:
            # each "line" in the file is a string
            limit = line[0].split("-")  # split the whole line at "-", to focus on the lower and upper limits for each password
            lower = limit[0] # first element of "limit"
            upper = limit[-1] # last element of "limit"
            letter = line[1].replace(":", "")
            password = line[-1]
            letter_count = password.count(letter)
            # since lower and upper are strings, we need to make the ints in order to use <=,>=
            if int(lower) <= letter_count <= int(upper):
                good_count += 1

        print(good_count)


find_valid_one("advent_2.csv")