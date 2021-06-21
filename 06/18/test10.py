responses = {}

flag = True
while flag:
    name = input("请输入你的名字？")
    response = input("一周内你最喜欢哪一天？")

    responses[name] = response

    repeat = input("请问还有人参与调查吗？yes / no")
    if repeat == 'no':
        flag = False
for name,response in responses.items():
    print(name,response)