# Create a class Car with a public variable brand and a public method start(). 
# Instantiate the class and access both from outside the class.
class Car:
    def __init__(self, brand):
        self.brand = brand

    def start (self):
        print(f"{self.brand} has started.")

my_car = Car("Ferrari")
print("Brand of  the Car:", my_car.brand)

my_car.start()
