#情况2：子类不需要自动调用父类的方法：子类重写__init__()方法，实例化子类后，将不会自动调用父类的__init__()的方法

class Father():
    def __init__(self,name):
        self.name = name
        print("name %s" % (self.name))
    def getName(self):
        return "Father" + self.name

class Son(Father):
    def __init__(self,name):
        print("hi")
        self.name = name
    def getName(self):
        return "Father" + self.name

if __name__ == "__main__":
    son = Son("张三")
    son.getName()

