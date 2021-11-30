# Part 2
import csv
# How many passwords are valid according to the new interpretation
def day_two(csv_file_name):
    with open("advent_2.csv", newline="") as csv_file:
        new_passwords = csv.reader(csv_file, delimiter=" ")
        good_password = 0
        bad_password = 0
# How many
        for line in new_passwords:
            constraint = line[0].split("-") # range of vals
            lower = constraint[0]
            upper = constraint[-1]
            letter = line[1].replace(":", "")
            password = line[-1]
           # letter_count = password.count(letter)
            # print(lower)
            # print(upper)
            # letter_count = 0
            if password[int(lower)-1] == letter and password[int(upper)-1] == letter:
                bad_password += 1
            elif password[int(lower)-1] == letter or password[int(upper)-1] == letter:
                good_password += 1
            else:
                bad_password += 1


        print(good_password)

day_two("advent_2.csv")