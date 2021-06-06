'''
dumps 是将字典转换为字符串。loads 是将字符串转换为字典
'''

import pickle
dict = {'a':1,"b":2}
dict1 = pickle.dumps(dict)
dict2 = pickle.loads(dict1)
print(dict)
print(dict1)
print(dict2)