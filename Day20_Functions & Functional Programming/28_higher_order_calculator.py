# Higher-order function calculator


def calculate(operation, a, b):
    return operation(a, b)


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"

    return a / b


print("Addition:", calculate(add, 20, 10))

print("Subtraction:", calculate(subtract, 20, 10))

print("Multiplication:", calculate(multiply, 20, 10))

print("Division:", calculate(divide, 20, 10))

print("Lambda Power:", calculate(lambda a, b: a ** b, 2, 3))

power = lambda a, b: a ** b
print("Power using lamda only:", power(2, 3))

print("Direct Lamda call:", (lambda a, b: a ** b)(2, 3))