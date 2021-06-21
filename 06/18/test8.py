# 在列表之间移动元素
list = ['apple','banana','orange','pear']
list1 = []

while list:
    res = list.pop()
    print({res.title()})
    list1.append(res)

    for i in list1:
        print(i.title())