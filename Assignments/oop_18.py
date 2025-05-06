# Property Decorators: @property, @setter, and @deleter

class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        print("Getting price ...")
        return self._price
    
    @price.setter
    def price(self, value):
        print("Setting Price....")
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price

p = Product(100)
print(p.price)
p.price = 130
print(p.price)
del p.price