#情况3：子类重写__init__()方法又需要调用父类的方法

class Father():
    def __init__(self,name):
        self.name = name
        print("name:%s" %(self.name))
    def getName(self):
        return ('Father' + self.name)

class Son(Father):
    def __init__(self,name):
        super(Son,self).__init__(name)
        print("hi")
        self.name = name
    def getName(self):
        return 'Son' + self.name
if __name__ == '__main__':
    son = Son('sunoob')
    print(son.getName())
