file_name = 'D:\\file.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

birthday = input("enter your bithday,in the form mmddyy")
if birthday in pi_string:
    print("you birthday in pi_string")
else:
    print("you birthday not in pi_string")

print(f"{ pi_string[:52] }")
print(len(pi_string))  #打印长度