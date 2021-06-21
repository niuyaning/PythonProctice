#定义可选形参

def build_person(first_name,last_name,age=None):
    person = {'first':first_name,'last':last_name}
    if age:
        person['age'] = age
    return person

res = build_person("牛","亚宁")
print(res)