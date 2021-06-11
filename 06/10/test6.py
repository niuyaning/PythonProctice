import threading,time
lock = threading.Lock()

'''
使用with加锁
'''

def count(i):
    time.sleep(1)
    with lock:
        print(i)

threads = []
for i in range(1000):
    thread = threading.Thread(target=count,args=(i,))
    threads.append(thread)
for thread in threads:
    thread.start()