import threading,queue
from urllib import request

url = "https://www.baidu.com"

q = queue.Queue()

for i in range(1000):
    q.put(i)

def get_baidu():
    while True:
        try:
            q.get(block=False)
            r = request.urlopen(url)
            print(r.code)
        except queue.Empty:
            break

ts = []
for i in range(100):
    t = threading.Thread(target=get_baidu())
    ts.append(t)
    t.start()

for i in ts:
    t.join()