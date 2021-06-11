from concurrent.futures import ThreadPoolExecutor
from urllib import request

url = "https://www.baidu.com"

def get_baidu():
    r = request.urlopen(url)
    print(r.code)

with ThreadPoolExecutor(max_workers=4) as executor:
    for i in range(100):
        executor.submit(get_baidu())