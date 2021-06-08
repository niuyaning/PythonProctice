def add_decorator(f):
    def wrap(x,y):
        print("加法")
        return f(x,y)
    return wrap

@add_decorator
def add_method(x,y):
    return x + y

print(add_method(2,3))