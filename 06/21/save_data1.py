import json
#存储用户姓名 name 到 file4.txt 中

file_name = "D:\\file4.txt"
name = input("请输入姓名：")
with open(file_name,'w') as f:
    json.dump(name,f)

#向已存储了名字的用户发出问候
with open(file_name) as f:
    name = json.load(f)
    print(f"welcome back,{name}")