# Program 26 - Basic Abstract Class
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass

# Payment() would raise TypeError because pay() is abstract.
