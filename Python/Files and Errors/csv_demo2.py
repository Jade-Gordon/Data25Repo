import csv

# firstname, lastname, email
def transform_user_details(csv_file_name):
    #store data in a list
    new_user_data =[]
    with open(csv_file_name, newline='') as csvfile:
        user_details_csv = csv.reader(csvfile, delimiter=",")

        for user in user_details_csv:
            # create new list
            transformation = []
            transformation.append(user[1].replace("\n", "")) # firstname
            transformation.append(user[2].replace("\n", "")) # lastname
            transformation.append(user[-1].replace("\n", "")) # email (at end)
            new_user_data.append(transformation)

    return new_user_data
# print(transform_user_details("user_details.csv"))
#Now create new csv file -> write in a new location, hence 2 args
def create_new_user_data_csv(old_user_data_file, new_file_name):
    new_user_data = transform_user_details(old_user_data_file) # only need 1 arg as t_u_d only has 1 arg
    with open(new_file_name, 'w', newline = '') as newfile:
        csv_writer = csv.writer(newfile)
        for user in new_user_data:
            print(user)
            csv_writer.writerow(user)

create_new_user_data_csv("user_details.csv", "new_user_data.csv")