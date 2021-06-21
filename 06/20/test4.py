#给属性指定默认值
class Car:
    def __init__(self):
        self.year = 12

    def get_year(self):
        print(f"This car is {self.year}")

car = Car()
car.year = 13
car.get_year()