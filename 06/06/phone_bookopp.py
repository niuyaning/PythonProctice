'''
实现一个简单的通讯录，包含增删改查
'''
record_id = 0
record_list = []


def input_record():
    name = input("请输入姓名：")
    phone = input("请输入电话：")
    record = {"name": name, "phone": phone}
    print(record)
    return record


'''
新增
'''
def add_record():
    record = input_record()
    global record_id
    record_id += 1
    record["record_id"] = record_id
    record_list.append(record)
    return "添加成功"


'''
查询
'''
def query_record(name):
    query_ids = []
    query_result = []
    for record in record_list:
        if record["name"] == name:
            query_ids.append(record["record_id"])
            query_result.append(record)
    return query_ids, query_result

'''
删除
'''
def delete_recoed(name):
    query_ids,query_result = query_record(name)
    if len(query_ids) == 0:
        print("不存在")
    else:
        if len(query_result) > 1:
            for record in query_result:
                print("{}\t{}\t{}".format(record["record_id"].record["name"],record["phone"]))
            record_id = input("请选择要删除的id")
            if record_id in query_ids:
                for record in record_list:
                    if int(record_id) == record["record_id"]:
                        record_list.remove(record)
            else:
                print("输入错误")
        else:
            print("{}\t{}\t{}".format(query_result[0]["record_id"],query_result[0]["name"],query_result[0]["phone"]))
            while True:
                s = input("是否确认删除? Y/N:")
                if s in ["Y","N"]:
                    if s == "Y":
                        record_list.remove(query_result[0])
                        print("删除成功")
                    else:
                        pass
                    break
                else:
                    print("输入错误")
'''
修改
'''
def change_record(name):
    query_ids, query_result = query_record(name)
    if len(query_ids) == 0:
        print("不存在")
    else:
        if len(query_result) > 1:
            for record in query_result:
                print("{}\t{}\t{}".format(record["record_id"],record["name"],record["phone"]))
            record_id = input("请选择要修改的id：")
            if int(record_id) in query_ids:
                for record in record_list:
                    if int(record_id) == record["record_id"]:
                        phone = input("请输入修改后的电话号码：")
                        record["phone"] = phone
                        print("修改成功")
                        break
            else:
                print("输入错误")
        else:
            print("{}\t{}\t{}".format(query_result[0]["record_id"],query_result[0]["name"],query_result[0]["phone"]))
            phone_number = input("请输入修改后的电话号码")
            query_result[0]["phone"] = phone_number
            print("修改成功")

if __name__ == "__main__":
    while True:
        menu = '''
        通讯录
        1.增加
        2.查询
        3.删除
        4.修改
        '''
        print(menu)
        s = input("请选择：")
        if s in ["1", "2", "3", "4"]:
            if s == "1":
                msg = add_record()
                print(msg)
            if s == "2":
                name = input("请输入姓名：")
                query_ids, query_result = query_record(name)
                if len(query_ids) == 0:
                    print("不存在")
                else:
                    for record in query_result:
                        print("{}\t{}\t{}".format(record["record_id"], record["name"], record["phone"]))
            if s == "3":
                name = input("请输入姓名:")
                delete_recoed(name)
            if s == "4":
                name = input("请输入姓名：")
                change_record(name)
            if s == "5":
                break
        else:
            print("输入错误")
            continue