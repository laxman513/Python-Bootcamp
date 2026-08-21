class InsufficientBalanceError(Exception):
    pass

class InvalidAmountError(Exception):
    pass

class BankAccount:
    def __init__(self, account_holder, opening_balance=0.0):
        if not account_holder.strip():
            raise ValueError("Account holder name cannot be empty")
        if opening_balance < 0:
            raise ValueError("Opening balance cannot be negative")
        self.account_holder = account_holder
        self.balance = float(opening_balance)

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Deposit must be greater than zero")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Withdrawal must be greater than zero")
        if amount > self.balance:
            raise InsufficientBalanceError("Insufficient balance")
        self.balance -= amount

    def show_balance(self):
        print(f"Account holder : {self.account_holder}")
        print(f"Balance        : ₹{self.balance:.2f}")

def read_amount(prompt):
    try:
        return float(input(prompt))
    except ValueError:
        raise InvalidAmountError("Please enter a valid numeric amount")

def main():
    print("=== Bank Account Management System ===")
    try:
        name = input("Enter account holder name: ")
        opening_balance = read_amount("Enter opening balance: ")
        account = BankAccount(name, opening_balance)

        while True:
            print("\n1. Show balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")
            choice = input("Choose an option: ")

            try:
                if choice == "1":
                    account.show_balance()
                elif choice == "2":
                    account.deposit(read_amount("Enter deposit amount: "))
                    print("Deposit successful.")
                elif choice == "3":
                    account.withdraw(read_amount("Enter withdrawal amount: "))
                    print("Withdrawal successful.")
                elif choice == "4":
                    print("Thank you for using the Bank Account Management System.")
                    break
                else:
                    print("Invalid menu option.")
            except (InvalidAmountError, InsufficientBalanceError) as error:
                print("Transaction failed:", error)
    except (ValueError, InvalidAmountError) as error:
        print("Account creation/input failed:", error)

if __name__ == "__main__":
    main()
