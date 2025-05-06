# Create a class MathUtils with a static method add(a, b) that returns the sum.
# No class or instance variables should be used.

class MathUtils:
    @staticmethod
    def add (a,b):
        return a + b
    
result = MathUtils.add(8,9)
print("Sum:" , result)



# Create a class Logger that prints a message when an object is created
# (constructor) and another message when it is destroyed (destructor).
class Logger:
    def __init__(self):
        print("Logger is created")

    def __del__(self):
        print("Logger is destroyed")

log = Logger()
