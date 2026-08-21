class InsufficientBalanceError(Exception):
    pass


class InvalidAmountError(Exception):
    pass


def withdraw(balance, amount):

    if amount <= 0:
        raise InvalidAmountError(
            "Withdrawal amount must be greater than zero"
        )

    if amount > balance:
        raise InsufficientBalanceError(
            "Insufficient balance"
        )

    return balance - amount


balance = 10000

try:

    balance = withdraw(balance, 15000)

    print("Withdrawal successful")
    print("Remaining balance:", balance)

except InvalidAmountError as error:

    print("Invalid amount:", error)

except InsufficientBalanceError as error:

    print("Insufficient balance:", error)