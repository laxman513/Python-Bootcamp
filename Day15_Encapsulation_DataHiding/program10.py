# Property setter with validation
class Employee:
    def __init__(self, salary):
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        if salary >= 10000:
            self.__salary = salary
        else:
            print("Invalid salary")

employee = Employee(50000)
employee.salary = 5000
print(employee.salary)
