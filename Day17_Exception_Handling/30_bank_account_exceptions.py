class InsufficientBalanceError(Exception):
    pass


class InvalidAmountError(Exception):
    pass


class BankAccount:

    def __init__(self, name, balance):

        if not name.strip():
            raise ValueError("Name cannot be empty")

        if balance < 0:
            raise ValueError("Balance cannot be negative")

        self.name = name
        self.balance = balance

    def deposit(self, amount):

        if amount <= 0:
            raise InvalidAmountError(
                "Deposit amount must be greater than zero"
            )

        self.balance += amount

    def withdraw(self, amount):

        if amount <= 0:
            raise InvalidAmountError(
                "Withdrawal amount must be greater than zero"
            )

        if amount > self.balance:
            raise InsufficientBalanceError(
                "Insufficient balance"
            )

        self.balance -= amount


try:

    account = BankAccount("Rahul", 10000)

    print("Account:", account.name)
    print("Initial balance:", account.balance)

    print("\nDepositing 5000")
    account.deposit(5000)
    print("Balance:", account.balance)

    print("\nWithdrawing 3000")
    account.withdraw(50000)
    print("Balance:", account.balance)

    print("\nWithdrawing 50000")
    account.withdraw(50000)

except InvalidAmountError as error:

    print("Invalid amount:", error)

except InsufficientBalanceError as error:

    print("Transaction failed:", error)

except ValueError as error:

    print("Account error:", error)

print("\nProgram completed")