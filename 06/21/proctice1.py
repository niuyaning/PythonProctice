file_name = 'D:\\file2.txt'

while True:
    name = input("请输入姓名：")
    print ("你好，欢迎光临")

    with open(file_name,'w') as file_object:
        file_object.write(name)