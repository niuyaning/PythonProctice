import queue
from urllib import request
from multiprocessing import Process,Queue
'''
队列
'''

url = "http://www.baidu.com"

q = Queue()
for i in range(100):
    q.put(i)

def get_baidu():
    while True:
        try:
            q.get(block=False)
            r = request.urlopen(url)
            print(r.code)
        except queue.Empty:
            break

if __name__ == "__main__":
    ps = []
    for i in range(4):
        p = Process(target=get_baidu())
        ps.append(p)
    for p in ps:
        p.start()
    for p in ps:
        p.join()
