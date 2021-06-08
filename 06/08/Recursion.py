'''
递归--阶乘
'''
def factorial(n):
    if n ==1:
        return n
    else:
        return n * factorial(n-1)

if __name__ == "__main__":
    print(factorial(1))

