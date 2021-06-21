file_name = 'D:\\file2.txt'

name = input("请输入姓名:")

with open(file_name,'w') as file_object:
    file_object.write(name)

