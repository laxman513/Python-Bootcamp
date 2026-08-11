# Program 37 - Real-World Payment System
from abc import ABC, abstractmethod

class Payment(ABC):
    def __init__(self, amount):
        self.amount = amount

    @abstractmethod
    def process(self):
        pass

class UPI(Payment):
    def process(self):
        print(f"Processing ₹{self.amount} through UPI")

class CreditCard(Payment):
    def process(self):
        print(f"Processing ₹{self.amount} through Credit Card")

class NetBanking(Payment):
    def process(self):
        print(f"Processing ₹{self.amount} through Net Banking")

payments = [UPI(1000), CreditCard(2500), NetBanking(5000)]

for payment in payments:
    payment.process()
