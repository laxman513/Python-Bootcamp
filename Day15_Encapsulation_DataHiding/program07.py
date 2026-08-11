# @property getter
class Employee:
    def __init__(self, salary):
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

employee = Employee(50000)
print(employee.salary)
