# Create a class TemperatureConverter with a static method.
#  celsius_to_fahrenheit(c) that returns the Fahrenheit value.

class TempratureConvertor:
    @staticmethod
    def celsius_to_farenheit(c):
        return (c *9/5) + 32
    
celsius = 50
farenheit = TempratureConvertor.celsius_to_farenheit(celsius)
print(f"{celsius}°C is equal to {farenheit}°F")