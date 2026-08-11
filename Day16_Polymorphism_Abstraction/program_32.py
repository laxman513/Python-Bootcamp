# Program 32 - Abstract Property
from abc import ABC, abstractmethod

class Employee(ABC):
    @property
    @abstractmethod
    def salary(self):
        pass

class Developer(Employee):
    def __init__(self, salary):
        self._salary = salary

    @property
    def salary(self):
        return self._salary

developer = Developer(50000)

print(developer.salary)
