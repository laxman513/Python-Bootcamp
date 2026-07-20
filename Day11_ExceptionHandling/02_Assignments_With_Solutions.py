"""
==========================================================
Day 11 - Exception Handling
Assignments with Solutions
==========================================================

Instructions:
1. Read the question.
2. Stop and solve it yourself.
3. Compare your solution with the one below.
"""

# ==========================================================
# Assignment 1
# ==========================================================

"""
Question:

Write a program to accept two numbers from the user.
Divide them.
Handle ZeroDivisionError.
"""

print("\nAssignment 1")
print("-" * 40)

# ---------------- Solution ----------------

try:
    num1 = int(input("Enter First Number : "))
    num2 = int(input("Enter Second Number: "))

    print("Result:", num1 / num2)

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Please enter valid integers.")


# ==========================================================
# Assignment 2
# ==========================================================

"""
Question:

Accept a number from the user.

If the user enters text instead of a number,
handle ValueError.
"""

print("\nAssignment 2")
print("-" * 40)

# ---------------- Solution ----------------

try:
    number = int(input("Enter Number: "))
    print("You entered:", number)

except ValueError:
    print("Invalid number.")


# ==========================================================
# Assignment 3
# ==========================================================

"""
Question:

Create a list with five elements.

Ask the user to enter an index.

Print the element.

Handle IndexError.
"""

print("\nAssignment 3")
print("-" * 40)

# ---------------- Solution ----------------

numbers = [10, 20, 30, 40, 50]

try:
    index = int(input("Enter Index: "))
    print("Element:", numbers[index])

except IndexError:
    print("Invalid Index.")

except ValueError:
    print("Please enter only integers.")


# ==========================================================
# Assignment 4
# ==========================================================

"""
Question:

Create a dictionary containing

id
name

Ask the user to enter a key.

Print the value.

Handle KeyError.
"""

print("\nAssignment 4")
print("-" * 40)

# ---------------- Solution ----------------

employee = {
    "id": 101,
    "name": "Laxman"
}

try:
    key = input("Enter Key: ")

    print(employee[key])

except KeyError:
    print("Key does not exist.")


# ==========================================================
# Assignment 5
# ==========================================================

"""
Question:

Accept age from the user.

If age is negative,

raise ValueError.
"""

print("\nAssignment 5")
print("-" * 40)

# ---------------- Solution ----------------

try:
    age = int(input("Enter Age: "))

    if age < 0:
        raise ValueError("Age cannot be negative.")

    print("Age:", age)

except ValueError as e:
    print(e)


# ==========================================================
# Assignment 6
# ==========================================================

"""
Question:

Accept marks from the user.

Marks should be between 0 and 100.

Otherwise raise ValueError.
"""

print("\nAssignment 6")
print("-" * 40)

# ---------------- Solution ----------------

try:

    marks = int(input("Enter Marks: "))

    if marks < 0 or marks > 100:
        raise ValueError("Marks should be between 0 and 100.")

    print("Marks:", marks)

except ValueError as e:
    print(e)


# ==========================================================
# Assignment 7
# ==========================================================

"""
Question:

Create a custom exception called

InvalidSalaryError

Raise it when salary is negative.
"""

print("\nAssignment 7")
print("-" * 40)

# ---------------- Solution ----------------

class InvalidSalaryError(Exception):
    pass

try:

    salary = float(input("Enter Salary: "))

    if salary < 0:
        raise InvalidSalaryError("Salary cannot be negative.")

    print("Salary:", salary)

except InvalidSalaryError as e:
    print(e)

except ValueError:
    print("Please enter a valid salary.")


# ==========================================================
# Assignment 8
# ==========================================================

"""
Question:

Write a program using

try
except
else
finally

Show the execution flow.
"""

print("\nAssignment 8")
print("-" * 40)

# ---------------- Solution ----------------

try:

    number = int(input("Enter Number: "))

    print("100 / Number =", 100 / number)

except ZeroDivisionError:
    print("Cannot divide by zero.")

except ValueError:
    print("Invalid number.")

else:
    print("No Exception Occurred.")

finally:
    print("Program Finished.")


# ==========================================================
# Assignment 9
# ==========================================================

"""
Question:

Open a file called

employee.txt

Handle FileNotFoundError.
"""

print("\nAssignment 9")
print("-" * 40)

# ---------------- Solution ----------------

try:

    file = open("employee.txt", "r")

    print(file.read())

    file.close()

except FileNotFoundError:
    print("employee.txt not found.")


# ==========================================================
# Assignment 10
# ==========================================================

"""
Question:

Create a Calculator.

Menu

1 Addition
2 Subtraction
3 Multiplication
4 Division

Handle

ValueError
ZeroDivisionError
"""

print("\nAssignment 10")
print("-" * 40)

# ---------------- Solution ----------------

try:

    print("Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = int(input("Enter Choice: "))

    num1 = float(input("Enter First Number : "))
    num2 = float(input("Enter Second Number: "))

    if choice == 1:
        print("Result:", num1 + num2)

    elif choice == 2:
        print("Result:", num1 - num2)

    elif choice == 3:
        print("Result:", num1 * num2)

    elif choice == 4:
        print("Result:", num1 / num2)

    else:
        print("Invalid Choice.")

except ValueError:
    print("Please enter valid numeric values.")

except ZeroDivisionError:
    print("Cannot divide by zero.")