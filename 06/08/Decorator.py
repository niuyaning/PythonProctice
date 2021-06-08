'''
装饰器
'''
# def deco(func):
#     def inner():
#         print("running inner()")
#     return inner
#
# @deco
# def target():
#     print('runner target()')
#
#
# if __name__ == "__main__":
#     target()

def deco(func):
    def inner():
        print("running inner")
    return inner

def target():
    print('running target()')

if __name__ == "__main__":
    target = deco(target)
    target()