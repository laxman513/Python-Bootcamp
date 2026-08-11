# Program 14 - Duck Typing with pay()
class CreditCard:
    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")

class Cash:
    def pay(self, amount):
        print(f"Paid ₹{amount} using Cash")

def make_payment(method, amount):
    method.pay(amount)

make_payment(CreditCard(), 1000)
make_payment(Cash(), 500)
