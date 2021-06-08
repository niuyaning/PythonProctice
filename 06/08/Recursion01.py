'''
递归 - x 的n次幂 等于x 的n-1次幂乘x，x的0次幂等于1
'''

def power(x,n):
    if n == 0:
        return 1
    else:
        return x * power(x,n-1)

if __name__ == "__main__":
    print(power(2,2))