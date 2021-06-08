'''
统计函数的执行时间
'''

import time

def decorator(func):
    def wrapper():
        start_time = time.time()

        func()

        end_time = time.time()

        print(end_time - start_time)

    return wrapper

@decorator
def sa():
    print("sa")


sa()