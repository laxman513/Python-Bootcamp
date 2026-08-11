# Program 33 - Abstract Employee System
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary

    def calculate_salary(self):
        return self.monthly_salary

class PartTimeEmployee(Employee):
    def __init__(self, name, hours, rate):
        super().__init__(name)
        self.hours = hours
        self.rate = rate

    def calculate_salary(self):
        return self.hours * self.rate

employees = [
    FullTimeEmployee("Rahul", 50000),
    PartTimeEmployee("Amit", 100, 500)
]

for employee in employees:
    print(employee.name, employee.calculate_salary())
