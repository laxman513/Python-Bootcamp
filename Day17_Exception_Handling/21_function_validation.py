def withdraw(balance, amount):

    if amount <= 0:
        raise ValueError("Amount must be greater than 0")

    if amount > balance:
        raise ValueError("Insufficient balance")

    return balance - amount

balance = 1000

try:
    balance = withdraw(balance, 3000)
    print("Withdraw successfull")
    print("Remain balance:", balance)

except ValueError as error:
    print("Withdrawal failed:", error)