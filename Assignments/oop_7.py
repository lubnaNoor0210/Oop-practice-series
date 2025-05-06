# Create a class Employee with:
# a public variable name,
# a protected variable \_salary, and
# a private variable \_\_ssn.
# Try accessing all three variables from an object of the class and document what happens.

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name         
        self._salary = salary    
        self.__ssn = ssn        

emp = Employee("John", 9000, "123-45-6789")

print("Name:", emp.name) 
print("Salary:", emp._salary) 

try:
    print("SSN:", emp.__ssn)
except AttributeError as e:
    print("Error accessing __ssn directly:", e)

print("SSN (via name mangling):", emp._Employee__ssn)

