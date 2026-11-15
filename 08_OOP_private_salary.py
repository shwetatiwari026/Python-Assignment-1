class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary  # Double underscore makes this a name-mangled attribute.

    def show_details(self):
        print("Employee:", self.name)
        print("Salary:", self.__salary)


employee = Employee("Aman", 30000)
employee.show_details()

# Accessing employee.__salary directly is intentionally not allowed.
