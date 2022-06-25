from user import User
from post import Post

app_user_one = User("pws","@mail.ru","Andrey","home")

app_user_one.get_user_info()

new_post = Post("Hello", app_user_one.get_name())
new_post.get_post_info()