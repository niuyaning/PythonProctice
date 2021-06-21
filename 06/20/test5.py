#通过方法修改属性的值

class Car:
    def update_odometer(self,mileage):
        self.odometer_reading += mileage
        print(f"公里数为 {self.odometer_reading}")

car = Car()
car.update_odometer(20)