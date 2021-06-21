users = {
    'name':{
       'first':'牛',
       'last':'亚宁',
        'location':'北京'
    },
    'age':{
        'first': '张',
        'last': '三',
        'location': '上海'
    }
}
for username,userinfo in users.items():
    full_name = f"{userinfo['first']}{userinfo['last']}"
    location = userinfo['location']

    print(f"full name:{full_name.title()}")
    print(f"location:{location.title()}")
