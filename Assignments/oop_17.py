# CLASS DECORATORS

def add_greeting(cls):
    def greet(self):
        return "Hello from decorator!"
    cls.greet = greet
    return cls

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

p = Person("George")
print(p.greet())