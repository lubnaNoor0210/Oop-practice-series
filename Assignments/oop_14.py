# Create a class Department and a class Employee.
# Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.
class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def get_details(self):
        return f"Employee Name: {self.name}, ID: {self.emp_id}"

class Department:
    def __init__(self, dept_name, employee):
        self.dept_name = dept_name
        self.employee = employee 
    def show_info(self):
        return f"Department: {self.dept_name}\n{self.employee.get_details()}"

emp = Employee("Fury", 200)
dept = Department("HR", emp)
print(dept.show_info())

