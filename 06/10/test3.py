#python 中函数参数 *args 和 ** kwargs

'''
普通参数
'''
def fun(name):

    print("hello" + name)

fun("world")


'''
默认参数
'''
def fun1(name, age = 1 ):
    print('hello',name,age,'年')
fun1("world")

'''
元组参数
'''
def fun(name,age=1,*args):
    print('hello',name,age,'年')
    print(args)

    for i in args:
        print(i)

fun('world',1,'I','love','it')

'''
字典参数
# '''
def fun(name,age=1,*args,**kwargs):
    print('Hello',name,age,'年')
    print(args)
    for i in args:
        print(i)
    print(kwargs)

    for m in kwargs:
        print(m,":",kwargs[m])

fun('world',1,'i','love','it',my = 'jack',like = 'apple')










