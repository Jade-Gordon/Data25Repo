# Inheriting from other files -> user_class, post
# importing a module
from user_class import User
from post import Post

app_user_one = User("jg@jg.com", "Jade Gordon", "pwd", "Junior Data engineer")
app_user_one.get_user_info()
# Different user:
app_user_two = User("rs@rs.com", "R S", "secret", "Data Analyst")
app_user_two.get_user_info() # gets user info from app_user_two

new_post = Post("Analysing Covid-related data today!", app_user_two.name)
new_post.get_post_info()