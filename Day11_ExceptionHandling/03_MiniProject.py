"""
==========================================================
Mini Project
Bank Account Management System
Day 11 - Exception Handling
==========================================================
"""

# ------------------------------------------
# Custom Exception
# ------------------------------------------

class InsufficientBalanceError(Exception):
    pass


# ------------------------------------------
# Initial Balance
# ------------------------------------------

balance = 10000.0


# ------------------------------------------
# Functions
# ------------------------------------------

def check_balance():
    print(f"\nCurrent Balance : ₹{balance:.2f}")


def deposit():

    global balance

    try:

        amount = float(input("Enter Deposit Amount: "))

        if amount <= 0:
            raise ValueError("Deposit amount must be greater than zero.")

        balance += amount

        print("Deposit Successful.")

    except ValueError as e:
        print(e)


def withdraw():

    global balance

    try:

        amount = float(input("Enter Withdrawal Amount: "))

        if amount <= 0:
            raise ValueError("Withdrawal amount must be greater than zero.")

        if amount > balance:
            raise InsufficientBalanceError("Insufficient Balance.")

        balance -= amount

        print("Withdrawal Successful.")

    except ValueError as e:
        print(e)

    except InsufficientBalanceError as e:
        print(e)


# ------------------------------------------
# Main Menu
# ------------------------------------------

while True:

    print("\n")
    print("=" * 45)
    print("      BANK ACCOUNT MANAGEMENT SYSTEM")
    print("=" * 45)

    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    try:

        choice = int(input("\nEnter Choice: "))

        if choice == 1:

            check_balance()

        elif choice == 2:

            deposit()

        elif choice == 3:

            withdraw()

        elif choice == 4:

            print("\nThank you for using the system.")
            break

        else:

            print("Invalid Choice.")

    except ValueError:

        print("Please enter a valid menu option.")

    finally:

        print("-" * 45)