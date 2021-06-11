'''
线程间同步
'''
import threading,time

def count(i):
    time.sleep(1)
    print(i)

threads = []
for i in range(1000):
    thread = threading.Thread(target=count,args=(i,))
    threads.append(thread)

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()