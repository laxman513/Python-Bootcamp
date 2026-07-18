# ============================================================
# Day 09 - Python Functions
# Part 1 (Programs 1 - 25)
# Author : Laxman
# ============================================================

print("=" * 60)
print("PROGRAM 1 - Simple Function")
print("=" * 60)

def greet():
    print("Hello Python")

greet()


print("\n" + "=" * 60)
print("PROGRAM 2 - Calling Function Twice")
print("=" * 60)

def greet():
    print("Hello")

greet()
greet()


print("\n" + "=" * 60)
print("PROGRAM 3 - Printing Function")
print("=" * 60)

def greet():
    print("Hello")

print(greet)


print("\n" + "=" * 60)
print("PROGRAM 4 - Function Type")
print("=" * 60)

def greet():
    print("Hello")

print(type(greet))


print("\n" + "=" * 60)
print("PROGRAM 5 - Calling Function")
print("=" * 60)

def greet():
    print("Hello")

greet()


print("\n" + "=" * 60)
print("PROGRAM 6 - Function Reference")
print("=" * 60)

def greet():
    print("Hello")

print(greet)
print(type(greet))


print("\n" + "=" * 60)
print("PROGRAM 7 - Multiple Calls")
print("=" * 60)

def greet():
    print("Hello")

greet()
greet()


print("\n" + "=" * 60)
print("PROGRAM 8 - Empty Function Using pass")
print("=" * 60)

def greet():
    pass

print("Function created successfully.")


print("\n" + "=" * 60)
print("PROGRAM 9 - Function Returning None")
print("=" * 60)

def greet():
    pass

print(greet())


print("\n" + "=" * 60)
print("PROGRAM 10 - Function with return")
print("=" * 60)

def greet():
    return "Hello"

print(greet())


print("\n" + "=" * 60)
print("PROGRAM 11 - print() vs return")
print("=" * 60)

def greet():
    print("Hello")

result = greet()
print(result)


print("\n" + "=" * 60)
print("PROGRAM 12 - Returning Addition")
print("=" * 60)

def add():
    return 10 + 20

print(add())


print("\n" + "=" * 60)
print("PROGRAM 13 - Returning Character")
print("=" * 60)

def grade():
    return "A"

print(grade())


print("\n" + "=" * 60)
print("PROGRAM 14 - Returning String")
print("=" * 60)

def message():
    return "Hello"

print(message())


print("\n" + "=" * 60)
print("PROGRAM 15 - Type of Function")
print("=" * 60)

def demo():
    return 100

print(type(demo))


print("\n" + "=" * 60)
print("PROGRAM 16 - Parameter Example")
print("=" * 60)

def greet(name):
    print("Hello", name)

greet("Laxman")


print("\n" + "=" * 60)
print("PROGRAM 17 - Different Argument")
print("=" * 60)

def greet(name):
    print("Hello", name)

greet("Rahul")


print("\n" + "=" * 60)
print("PROGRAM 18 - Two Parameters")
print("=" * 60)

def add(a, b):
    print(a + b)

add(10, 20)


print("\n" + "=" * 60)
print("PROGRAM 19 - Multiplication")
print("=" * 60)

def multiply(a, b):
    print(a * b)

multiply(10, 30)


print("\n" + "=" * 60)
print("PROGRAM 20 - String Parameter")
print("=" * 60)

def greet(language):
    print("Hello", language)

greet("Python")


print("\n" + "=" * 60)
print("PROGRAM 21 - Default Parameter")
print("=" * 60)

def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Laxman")


print("\n" + "=" * 60)
print("PROGRAM 22 - Default Parameters")
print("=" * 60)

def add(a=10, b=20):
    print(a + b)

add()


print("\n" + "=" * 60)
print("PROGRAM 23 - Default Parameter Override")
print("=" * 60)

def multiply(a=10, b=12):
    print(a * b)

multiply()
multiply(10, 20)


print("\n" + "=" * 60)
print("PROGRAM 24 - Keyword Arguments")
print("=" * 60)

def multiply(a, b):
    print(a * b)

multiply(b=30, a=10)


print("\n" + "=" * 60)
print("PROGRAM 25 - Keyword Arguments Example")
print("=" * 60)

def employee(name, city):
    print(name, city)

employee(name="Laxman", city="Hyderabad")

print("\n")
print("=" * 60)
print("End of Day09_Programs.py - Part 1")
print("=" * 60)