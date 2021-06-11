import threading,time
'''
线程加锁
'''
lock = threading.Lock()

def count(i):
    time.sleep(1)
    lock.acquire()
    print(i)
    lock.release()
threads = []

for i in range(1000):
    thread = threading.Thread(target=count,args=(i,))
    threads.append(thread)

for thread in threads:
    thread.start()