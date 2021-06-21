#遍历字典
dict = {
    'firstname':'牛',
    'lastname':'亚宁',
    'age':30,
    'city':'邯郸'}

for key,value in dict.items():
    print(f"\nKey:{key}")
    print(f"\nValue:{value}")


favorite_langrages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python'
}
for name,language in favorite_langrages.items():
    print(f"{name.title()}'s favorite language is {language.title()}" )

