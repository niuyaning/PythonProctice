class Restaurant:
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name,
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} name is chinese food'")
        print(f"{self.cuisine_type} is chuancai")

    def open_restaurant(self):
        print("欢迎光临，餐馆正在营业")

r = Restaurant("chinese food","chuancai")
r.describe_restaurant()
r.open_restaurant()


