#json.dump 写入文件

import json

numbers = [2,3,5,7,9]
filename = 'D:\\file4.txt'

with open(filename,'w') as f:
    json.dump(numbers,f)

with open(filename,) as f:
    numbers = json.load(f)

print(numbers)