# Program 07 - Polymorphism with Payment Types
class Payment:
    def pay(self):
        print("Processing payment")

class UPI(Payment):
    def pay(self):
        print("Payment using UPI")

class CreditCard(Payment):
    def pay(self):
        print("Payment using Credit Card")

class PayPal(Payment):
    def pay(self):
        print("Payment using PayPal")

payments = [UPI(), CreditCard(), PayPal()]

for payment in payments:
    payment.pay()
