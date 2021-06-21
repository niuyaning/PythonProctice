#将实例用作属性
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


class Battery():
    def __init__(self,battery_size = 75):
        self.battery_size = battery_size

    def battery_size(self):
        print(f"This car has a {self.battery_size} battery")

class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery()

my_tesla = ElectricCar('tesla','modek s ',2019)
my_tesla.battery.battery_size()