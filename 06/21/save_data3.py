import json

file_name = "D:\\username.json"
def get_stored_username():
    try:
        with open(file_name, ) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username
def get_user():
    username = get_stored_username()
    if username:
        print(f"welcome back,{username}")
    else:
        username = input("请输入你的名字？")
        with open(file_name,'w') as f:
            json.dump(username,f)
            print(f"{username}")
get_user()




