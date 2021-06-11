from concurrent.futures import ProcessPoolExecutor
from urllib import request

url = "https://www.baidu.com"

def get_baidu():
    r = request.urlopen(url)
    print(r.code)

if __name__ == "__main__":
    with ProcessPoolExecutor(max_workers=4) as executor:
        for i in range(100):
            executor.submit(get_baidu())