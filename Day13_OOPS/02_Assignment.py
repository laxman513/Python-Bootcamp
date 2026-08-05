"""
==========================================================
Day 13 Assignment - Object Oriented Programming (OOP)
==========================================================

Instructions

1. Try to solve every question yourself.
2. Solutions are provided at the bottom.
3. Compare your solution only after attempting.
"""

print("\n================ Assignment 1 ================")

"""
Assignment 1

Create a Student class.

Instance Variables
------------------
name
age

Create an object and display both values.
"""

# ---------------- Solution ----------------

class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age


student = Student("Laxman", 44)

print(student.name)
print(student.age)


print("\n================ Assignment 2 ================")

"""
Assignment 2

Create an Employee class.

Variables

id
name
salary

Display employee details.
"""

# ---------------- Solution ----------------

class Employee:

    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary

    def display(self):
        print("ID :", self.emp_id)
        print("Name :", self.name)
        print("Salary :", self.salary)


employee = Employee(101, "Laxman", 250000)

employee.display()


print("\n================ Assignment 3 ================")

"""
Assignment 3

Create Car class.

Methods

start()

stop()
"""

# ---------------- Solution ----------------

class Car:

    def start(self):
        print("Car Started")

    def stop(self):
        print("Car Stopped")


car = Car()

car.start()

car.stop()


print("\n================ Assignment 4 ================")

"""
Assignment 4

Rectangle

length

width

Method

area()
"""

# ---------------- Solution ----------------

class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


rectangle = Rectangle(10, 20)

print("Area :", rectangle.area())


print("\n================ Assignment 5 ================")

"""
Bank Account

deposit()

withdraw()

display_balance()
"""

# ---------------- Solution ----------------

class BankAccount:

    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):

        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient Balance")

    def display_balance(self):
        print("Balance :", self.balance)


account = BankAccount(10000)

account.deposit(5000)

account.withdraw(3000)

account.display_balance()


print("\n================ Assignment 6 ================")

"""
Class Variable
"""

# ---------------- Solution ----------------

class Employee:

    company = "JP Morgan"

    def __init__(self, name):
        self.name = name


employee1 = Employee("Laxman")
employee2 = Employee("Rahul")

print(employee1.company)

print(employee2.company)

print(Employee.company)


print("\n================ Assignment 7 ================")

"""
Modify Class Variable
"""

# ---------------- Solution ----------------

Employee.company = "Google"

print(employee1.company)

print(employee2.company)

print(Employee.company)


print("\n================ Assignment 8 ================")

"""
Create Class Method

change_company()
"""

# ---------------- Solution ----------------

class Company:

    company = "Google"

    @classmethod
    def change_company(cls):
        cls.company = "Microsoft"


Company.change_company()

print(Company.company)


print("\n================ Assignment 9 ================")

"""
Create Static Method

is_even()
"""

# ---------------- Solution ----------------

class Number:

    @staticmethod
    def is_even(number):
        return number % 2 == 0


print(Number.is_even(10))

print(Number.is_even(15))


print("\n================ Assignment 10 ================")

"""
Calculator

add()

subtract()

multiply()
"""

# ---------------- Solution ----------------

class Calculator:

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b


print(Calculator.add(10, 20))

print(Calculator.subtract(20, 5))

print(Calculator.multiply(10, 5))


print("\n================ Bonus Assignment ================")

"""
Circle

radius

area()

circumference()
"""

# ---------------- Solution ----------------

class Circle:

    PI = 3.14159

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return Circle.PI * self.radius * self.radius

    def circumference(self):
        return 2 * Circle.PI * self.radius


circle = Circle(5)

print("Area :", circle.area())

print("Circumference :", circle.circumference())