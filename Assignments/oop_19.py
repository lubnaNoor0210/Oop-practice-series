# callable() and __call__()

class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return value * self.factor
    
multiplier = Multiplier(8)
print(callable(multiplier))
result = multiplier(7)
print(result)