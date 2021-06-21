message = ['hello','welcome','beijing']
move_message = []

def show_message():
    for msg in message:
        print(msg)
        move_message.append(msg)
        print(move_message)


show_message()



