class Car:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def get_describe_name(self):
        long_name = f"{self.make,self.model,self.year}"
        return long_name.title()

car = Car('AUDI','a4',2019)
print(car.get_describe_name())