#  Creating a Custom Exception

class InvalidAgeError(Exception):
    def __init__(self, message="Age must be 18 or older"):
        self.message = message
        super().__init__(self.message)

def check_age(age):
    if age < 18:
        raise InvalidAgeError(f"Invalid age: {age}. You must be 18 or older.")
    else:
        print(f"Age {age} is valid.")

try:
    check_age(9)  
except InvalidAgeError as e:
    print(f"Error: {e}")
