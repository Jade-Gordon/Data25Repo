import os

working_directory = os.getcwd()
print(working_directory)

def return_user_id():
    # get user id -> see who's logged on
    print(os.uname())

return_user_id()