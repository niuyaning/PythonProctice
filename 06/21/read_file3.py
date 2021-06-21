file_name = 'D:\\file.txt'


with open(file_name) as file_object:
   lines = file_object.readlines()

pi_string = ''
for i in range(0,3):
   for line in lines:
     pi_string += line.strip() + "\n"

for i in range(0,len(pi_string)):
    print(pi_string[i], end = "")

print(f"{pi_string}")
