#获取用户名

def get_user_name(firstname,lastname,middlename=''):
    if middlename:
        full_name = (f'{firstname}{lastname}{middlename}')
    else:
        full_name = (f'{firstname}{lastname}')

    return full_name
