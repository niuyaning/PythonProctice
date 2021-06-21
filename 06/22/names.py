from users import get_user_name

while True:
    first = input("plaase give me a first name:")
    if first == 'q':
        break
    last = input("plase give me a last name:")
    if last == 'q':
        break

    full = get_user_name(first,last)
    print(f'{full}')