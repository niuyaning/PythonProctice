favorite_fruit = {
    'michael':'苹果',
    'summer':'香蕉',
    'andrew':'橙子'
}
for key,value in favorite_fruit.items():
    print(f"{key.title()} 最喜欢吃的水果是 {value.title()}")
    for result in favorite_fruit:
        print(result.title())