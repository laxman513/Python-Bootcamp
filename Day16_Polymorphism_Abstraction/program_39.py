# Program 39 - Add Payment Types
from abc import ABC, abstractmethod

class Payment(ABC):
    def __init__(self, amount):
        self.__amount = amount

    @property
    def amount(self):
        return self.__amount

    @abstractmethod
    def process(self):
        pass

class UPI(Payment):
    def process(self):
        print(f"Processing ₹{self.amount} through UPI")

class CreditCard(Payment):
    def process(self):
        print(f"Processing ₹{self.amount} through Credit Card")

payments = [UPI(1000), CreditCard(2500)]

for payment in payments:
    payment.process()
