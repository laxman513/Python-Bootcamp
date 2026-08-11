# Program 05 - Method Overriding
class Payment:
    def pay(self):
        print("Processing payment")

class UPI(Payment):
    def pay(self):
        print("Payment using UPI")

class CreditCard(Payment):
    def pay(self):
        print("Payment using Credit Card")

for payment in [UPI(), CreditCard()]:
    payment.pay()
