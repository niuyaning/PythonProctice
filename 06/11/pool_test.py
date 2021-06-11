'''
进程池
'''
from multiprocessing import Pool
import time

def func(num):
    print("hello world %d" % num)
    time.sleep(1)

if __name__ == "__main__":
    pool = Pool(processes=4)

    for i in range(100):
        pool.apply_async(func,(i,))

    pool.close()
    pool.join()