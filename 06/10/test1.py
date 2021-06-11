'''
多线程
'''
import time
import threading
'''
不同任务并行
'''
def helloworld():
    time.sleep(2)
    print("hello world")

t = threading.Thread(target = helloworld )
t.start()
print("threading ....")

