# Program 36 - Abstract Property + Polymorphism
from abc import ABC, abstractmethod

class Employee(ABC):
    @property
    @abstractmethod
    def salary(self):
        pass

class FullTimeEmployee(Employee):
    def __init__(self, salary):
        self._salary = salary

    @property
    def salary(self):
        return self._salary

class PartTimeEmployee(Employee):
    def __init__(self, hours, rate):
        self.hours = hours
        self.rate = rate

    @property
    def salary(self):
        return self.hours * self.rate

employees = [
    FullTimeEmployee(50000),
    PartTimeEmployee(80, 500)
]

for employee in employees:
    print(employee.salary)
