class InsufficientBalanceError(Exception):
    pass


def withdraw(balance, amount):

    if amount > balance:
        raise InsufficientBalanceError(
            "Insufficient balance for withdrawal"
        )

    return balance - amount


try:
    balance = 10000

    balance = withdraw(balance, 15000)

    print("Remaining balance:", balance)

except InsufficientBalanceError as error:
    print("Withdrawal failed:", error)