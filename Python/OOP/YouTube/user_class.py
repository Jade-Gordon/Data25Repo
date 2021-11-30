# refer to the "youtube_objects_and_classes.py" file
class User:
# object constructor info
    def __init__(self, user_email, name, password, current_job_title):
    # attributes for the User class
        self.email = user_email
        self.name = name
        self.password = password
        self.current_job_title = current_job_title

    def change_password(self, new_password):
        self.password = new_password

    def change_job_title(self, new_job_title):
        self.current_job_title = new_job_title

    def get_user_info(self):
        print(f"User {self.name} currently works as a {self.current_job_title}. "
              f"You can contact them at {self.email}")
## create object
## same syntax as calling a func
## the constructor expects 4 parameters -> def __init__(self,__,__,__,__):
## Now providing info for those parameters
## This has now constructed a new object for the User class
# User("jg@jg.com", "Jade Gordon", "pwd", "Junior Data engineer")
## Using the get_user_info method, we can now print the info about a user
app_user_one = User("jg@jg.com", "Jade Gordon", "pwd", "Junior Data engineer")
app_user_one.get_user_info()
# This prints: User Jade Gordon currently works as a Junior Data Engineer. You can contact them at jg@jg.com
# Changing the the job title of app_user one:
app_user_one.change_job_title("Data Engineer")
app_user_one.get_user_info() # calling the func that gets the user info
# Different user:
app_user_two = User("rs@rs.com", "R S", "secret", "Data Analyst")
app_user_two.get_user_info() # gets user info from app_user_two


