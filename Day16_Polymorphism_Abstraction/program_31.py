# Program 31 - Abstract Class + Polymorphism
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass

class UPI(Payment):
    def pay(self):
        print("Paid using UPI")

class CreditCard(Payment):
    def pay(self):
        print("Paid using Credit Card")

class Cash(Payment):
    def pay(self):
        print("Paid using Cash")

payments = [UPI(), CreditCard(), Cash()]

for payment in payments:
    payment.pay()
