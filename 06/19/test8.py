def get_name(first_name,last_name):
    full_name = (f"{first_name},{last_name}")
    return full_name

while True:
    f_name = input("请输入你的first_name:")
    if f_name == 'q':
        break
    l_name = input("请输入你的last_name:")
    if l_name == 'q':
        break
    f_name = get_name(f_name,l_name)
    print(f"\n Hello\n{f_name}")
