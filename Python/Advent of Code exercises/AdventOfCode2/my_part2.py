# Part 2
import csv
# How many passwords are valid according to the new interpretation
def find_valid_two(csv_file_name):
    with open("advent_2.csv", newline="") as csv_file:
        find_passwords = csv.reader(csv_file, delimiter=" ")
        good_count = 0
        bad_count = 0

        for line in find_passwords:
            limit = line[0].split("-") # range of vals
            lower = limit[0]
            upper = limit[-1]
            letter = line[1].replace(":", "")
            password = line[-1]
           # letter_count = password.count(letter)
            # print(lower)
            # print(upper)
            # letter_count = 0
            if password[int(lower)-1] == letter and password[int(upper)-1] == letter:
                bad_count += 1
            elif password[int(lower)-1] == letter or password[int(upper)-1] == letter:
                good_count += 1
            else:
                bad_count += 1


        print(good_count)

find_valid_two("advent_2.csv")