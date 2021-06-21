#定义父类 Car
class Car:
    #定义父类属性 make,model,year,odometer_reading=0
    def __init__(self,make,model,year):
        self.make = make,
        self.model = model,
        self.year = year,
        self.odometer_reading = 0
    #定义获取属性 make,model,year 的方法
    def get_descriptive_name(self):
        long_name = f"{self.make}{self.model}{self.year}"
        return long_name.title()
    #定义获取属性 odometer_reading=0 的方法
    def read_odometer(self):
        print(f'Thid car has {self.odometer_reading} miles on it')
    #修改父类属性 odometer_reading
    def update_odometer(self,mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading == mileage
        else:
            print("You can not roll back an odometer")
    def increment_odometer(self,miles):
        self.odometer_reading += miles

class ElectricCar(Car):
    def fill_gas_tank(self):
        print("This car does not need a gas tank")

# #定义子类 ElectricCar
# class ElectricCar(Car):
#     def __init__(self,make,model,year):
#         #继承 父类属性
#         super().__init__(make,model,year)
#         self.buttery_size = 75
#     def describe_buttery_size(self):
#         print(f"This car has a {self.buttery_size} kwh battery")
#
# #实例化子类
# my_tesla = ElectricCar('tesla','model s',2019)
#
# #调用子类 describe_buttery_size 方法
# my_tesla.describe_buttery_size()
#
# #调用父类获取属性 get_descriptive_name 方法
# print(my_tesla.get_descriptive_name())
