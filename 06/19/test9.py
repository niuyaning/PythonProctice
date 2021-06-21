#传递列表

def greet_users(names):
    for name in names:
        msg = f"Hello,{name.title()}"
        print(msg)
usernames = ['summer','michael','andrew']
greet_users(usernames)