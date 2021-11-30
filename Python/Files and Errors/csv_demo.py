# import csv library
import csv
with open("user_details.csv", newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
   #print(csvreader)
    iterable_csv = iter(csvreader)
    #next(iterable_csv)
    # counter = 0

    # for row in csvreader:
    #     print(row[-1]) # this prints the "email" (last) column
# what if we don't want the header
# cast as a list. Task: loop through it
    csv_list = list(csvreader)
    print(csv_list[1: -1])
    for row in iterable_csv: # this will get rid of the first row
        print(row)
        # if counter == 0:
        #     pass
        # else:
        #     print(row[-1])
        # counter += 1