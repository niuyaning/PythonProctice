import json


def getUser():
    file_name = "D:\\username.json"
    try:
        with open(file_name) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input("请输入名字：")
        with open(file_name, 'w') as f:
            json.dump(username, f)
            print(f"{username}")
    else:
        print(f"欢迎回来{username}")


getUser()
