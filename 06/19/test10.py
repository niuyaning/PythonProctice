#在函数中移动列表

old_fruit = ['banbana','orange','apple']
new_fruit = []

while old_fruit:
    fruit = old_fruit.pop()
    print(f"{fruit}")
    new_fruit.append(fruit)

for n in new_fruit:
    print(n)

