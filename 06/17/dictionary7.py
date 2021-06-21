#在字典中存储列表

pizza = {
    'crust':'thick',
    'topping':['mush','extra']
}
print(pizza['crust'])

for top in pizza['topping']:
    print(top)