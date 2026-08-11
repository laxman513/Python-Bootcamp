# Program 27 - Implementing an Abstract Method
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass

class UPI(Payment):
    def pay(self):
        print("Payment using UPI")

class CreditCard(Payment):
    def pay(self):
        print("Payment using Credit Card")

UPI().pay()
CreditCard().pay()
