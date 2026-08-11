# Program 09 - Using super() with Overriding
class Payment:
    def pay(self):
        print("Processing payment")

class UPI(Payment):
    def pay(self):
        super().pay()
        print("Payment using UPI")

UPI().pay()
