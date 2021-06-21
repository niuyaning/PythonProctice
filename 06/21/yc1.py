while True:
    first_number = input("First_number:")
    if first_number == 'q':
        break
    second_number = input("Second_number")

    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("you can not divide by 0")
    else:
        print(answer)
