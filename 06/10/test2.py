'''
同种任务并行
'''

import threading
import time

def helloworld(id):
    time.sleep(2)
    print("thread %d helloworld" % id)

for i in range(5):
    t = threading.Thread(target=helloworld,args=(i,))
    t.start()

print("main thread")
