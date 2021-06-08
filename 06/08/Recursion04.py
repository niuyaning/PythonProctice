'''
带参数的装饰器
'''

def out_f(arg):
    print("out_f" + arg)

    def decorator(func):
        def inner():
            func()
        return inner
    return decorator

@out_f("123")
def func():
    print("hello world")

func()