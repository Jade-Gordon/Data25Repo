import csv
# part 1
# eg valid password policy:   1-3 a: abcde
#                       the password must contain 1 <= "a" >= 3
# Q: How many passwords are valid?
def find_valid_one(csv_file_name):
    with open("advent_2.csv", newline="") as csv_file:
        find_passwords = csv.reader(csv_file, delimiter=" ")
        good_password = 0 # to count how many valid passwords there are

        for line in find_passwords:
            constraint = line[0].split("-") # each "line" in the file is a string
            lower = constraint[0] # e.g 1 <= a
            upper = constraint[-1] # e.g. a =< 3
            letter = line[1].replace(":", "")
            password = line[-1]
            letter_count = password.count(letter)
            # print(lower)
            # print(upper)
            # letter_count = 0
            if int(lower) <= letter_count <= int(upper):
                good_password += 1

        print(good_password)

find_valid_one("advent_2.csv")

