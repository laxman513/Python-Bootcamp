class BankAccount:

    def __init__(self, name, account_number, balance):
        self.__name = name
        self.__account_number = account_number
        self.__balance = balance

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name.strip():
            self.__name = name
        else:
            print("Name can not be empty")

    @property
    def account_number(self):
        return self.__account_number

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            print("Balance can not be negative")

    def deposit(self, amount):
        if amount >= 0:
            self.__balance += amount
            print("Amount depoisted successfully")
        else:
            print("Amount should not be negative")

    def withdraw(self, amount):
        if amount <= 0:
            print("Ivalid amount")

        elif amount > self.__balance:
            print("Insufficient balance")

        else:
            self.__balance -= amount
            print("Withdrawal successfull")

    @property
    def account_summary(self):
        return f"{self.__name} - {self.__account_number} - Balance: {self.__balance}"
        

account = BankAccount("Rahul", "ACC101", 10000)

print(account.name)
print(account.account_number)
print(account.balance)

print("-" * 30)
account.name = "Amit"
account.balance = 15000

print(account.name)
print(account.balance)

print("*" * 30)

account.name = "   "
account.balance = -5000

print("Depoiting 5000")

account.deposit(5000)
print(account.balance)

print("Depoiting -5000")

account.deposit(-5000)
print(account.balance)

print("Withdraw -5000")

account.withdraw(-5000)
print(account.balance)

print("Withdraw 500000")

account.withdraw(500000)
print(account.balance)

print("Withdraw 1000")

account.withdraw(1000)
print(account.balance)

print("Account Summary")
print(account.account_summary)

print("Using inheritance")
print("@" * 30)

class SavingsAccount(BankAccount):

    def __init__(self, name, account_number, balance, interest_rate):
        super().__init__(name, account_number, balance)
        self.__interest_rate = interest_rate

    @property
    def interest_rate(self):
        return self.__interest_rate

    @interest_rate.setter
    def interest_rate(self, value):
        if value >= 0:
            self.__interest_rate = value
        else:
            print("Interest rate cannot be negative")

    @property
    def interest(self):
        return self.balance * self.interest_rate / 100

account1 = SavingsAccount("Rahul", "SAV101", 20000, 5)

print(account1.name)
print(account1.account_number)
print(account1.balance)
print(account1.interest_rate)

account1.deposit(10000)

print(account1.balance)
print(account1.interest)