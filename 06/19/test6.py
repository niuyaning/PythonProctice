def get_name(first_name,last_name,middle_name=''):
    if middle_name:
        full_name = f"{first_name}{middle_name}{last_name}"
    else:
        full_name = f"{first_name}{last_name}"

    return full_name.title()

res = get_name('a','b')
print(res)

res1 = get_name('a','b','c')
print(res1)
