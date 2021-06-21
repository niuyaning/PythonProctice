#使用任意数量的关键字实参
def information(first_name,last_name,**userinfo):
    userinfo['first_name'] = first_name
    userinfo['last_name'] = last_name
    return userinfo

user_information = information(
    'summer','michael',
    location = '北京',
    sex = '女'
)

print(user_information)