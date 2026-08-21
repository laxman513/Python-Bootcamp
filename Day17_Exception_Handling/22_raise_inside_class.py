class BankAccount:

    def __init__(self, name, balance):

        if not name.strip():
            raise ValueError("Name can not be empty")

        if balance < 0:
            raise ValueError("Balance can not be negative")
        
        self.name = name
        self.balance = balance

    def deposit(self, amount):

        if amount <= 0 :
            raise ValueError("Deposit amount must be greater than zero")

        self.balance += amount

try:

    account = BankAccount("Laxman", 1000)
    account.deposit(500)

    print("Account Name:", account.name)
    print("Account Balance:", account.balance)

except ValueError as error:
      print("Account error:", error)