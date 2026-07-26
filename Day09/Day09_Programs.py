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

print("\n" + "=" * 60)
print("PROGRAM 26 - Keyword Arguments")
print("=" * 60)

def employee(name="Guest", city="Hyderabad"):
    print(name, city)

employee()


print("\n" + "=" * 60)
print("PROGRAM 27 - Keyword Arguments")
print("=" * 60)

def employee(name, city):
    print(name, city)

employee(name="Laxman", city="Hyderabad")


print("\n" + "=" * 60)
print("PROGRAM 28 - Keyword Arguments (Order Changed)")
print("=" * 60)

employee(city="Hyderabad", name="Laxman")


print("\n" + "=" * 60)
print("PROGRAM 29 - Positional Arguments")
print("=" * 60)

def add(a, b):
    print(a + b)

add(10, 20)


print("\n" + "=" * 60)
print("PROGRAM 30 - Mixed Arguments")
print("=" * 60)

employee("Laxman", city="Hyderabad")


print("\n" + "=" * 60)
print("PROGRAM 31 - Keyword Only Call")
print("=" * 60)

employee(name="Laxman", city="Hyderabad")


print("\n" + "=" * 60)
print("PROGRAM 32 - Positional Arguments")
print("=" * 60)

def details(name, age):
    print(name, age)

details("Laxman", 46)


print("\n" + "=" * 60)
print("PROGRAM 33 - Keyword Arguments")
print("=" * 60)

details(age=46, name="Laxman")


print("\n" + "=" * 60)
print("PROGRAM 34 - Invalid Example")
print("=" * 60)

print("Positional arguments cannot come after keyword arguments.")
# details(name="Laxman", 46)   # Invalid


print("\n" + "=" * 60)
print("PROGRAM 35 - Positional Arguments")
print("=" * 60)

details("Laxman", age=46)


print("\n" + "=" * 60)
print("PROGRAM 36 - Default Parameters")
print("=" * 60)

def person(name="Guest", age=18):
    print(name, age)

person()


print("\n" + "=" * 60)
print("PROGRAM 37 - *args (No Arguments)")
print("=" * 60)

def demo(*args):
    print(args)

demo()


print("\n" + "=" * 60)
print("PROGRAM 38 - *args (One Argument)")
print("=" * 60)

demo(10)


print("\n" + "=" * 60)
print("PROGRAM 39 - *args (Multiple Arguments)")
print("=" * 60)

demo(10, 20)


print("\n" + "=" * 60)
print("PROGRAM 40 - Type of args")
print("=" * 60)

def sample(*args):
    print(type(args))

sample(10, 20, 30)


print("\n" + "=" * 60)
print("PROGRAM 41 - len(args)")
print("=" * 60)

def count(*args):
    print(len(args))

count(1, 2, 3, 4, 5)


print("\n" + "=" * 60)
print("PROGRAM 42 - Sum Using *args")
print("=" * 60)

def total(*numbers):
    print(sum(numbers))

total(10, 20, 30, 40)


print("\n" + "=" * 60)
print("PROGRAM 43 - Multiplication")
print("=" * 60)

def multiply(*numbers):
    result = 1
    for num in numbers:
        result *= num
    print(result)

multiply(10, 20)


print("\n" + "=" * 60)
print("PROGRAM 44 - Sum of Three Numbers")
print("=" * 60)

total(10, 20, 30)


print("\n" + "=" * 60)
print("PROGRAM 45 - **kwargs")
print("=" * 60)

def demo(**kwargs):
    print(kwargs)

demo()


print("\n" + "=" * 60)
print("PROGRAM 46 - **kwargs (One Item)")
print("=" * 60)

demo(name="Laxman")


print("\n" + "=" * 60)
print("PROGRAM 47 - **kwargs (Multiple Items)")
print("=" * 60)

demo(name="Laxman", age=46)


print("\n" + "=" * 60)
print("PROGRAM 48 - Type of kwargs")
print("=" * 60)

def info(**kwargs):
    print(type(kwargs))

info(name="Laxman")


print("\n" + "=" * 60)
print("PROGRAM 49 - Access Dictionary Value")
print("=" * 60)

def student(**kwargs):
    print(kwargs["name"])

student(name="Laxman")


print("\n" + "=" * 60)
print("PROGRAM 50 - Dictionary Keys")
print("=" * 60)

def employee_details(**kwargs):
    print(kwargs.keys())

employee_details(name="Laxman", age=46, city="Hyderabad")

print("\n")
print("=" * 60)
print("End of Day09_Programs.py - Part 2")
print("=" * 60)

print("\n" + "=" * 60)
print("PROGRAM 51 - Dictionary Length")
print("=" * 60)

student = {
    "name": "Laxman",
    "age": 46,
    "city": "Hyderabad"
}

print(len(student))


print("\n" + "=" * 60)
print("PROGRAM 52 - Local Variable")
print("=" * 60)

def greet():
    message = "Hello"
    print(message)

greet()


print("\n" + "=" * 60)
print("PROGRAM 53 - Local Variable Scope")
print("=" * 60)

def greet():
    message = "Hello"

greet()

try:
    print(message)
except NameError as e:
    print(e)


print("\n" + "=" * 60)
print("PROGRAM 54 - Global Variable")
print("=" * 60)

city = "Hyderabad"

def demo():
    print(city)

demo()


print("\n" + "=" * 60)
print("PROGRAM 55 - Local vs Global Variable")
print("=" * 60)

city = "Hyderabad"

def demo():
    city = "Bangalore"
    print(city)

demo()
print(city)


print("\n" + "=" * 60)
print("PROGRAM 56 - Reading Global Variable")
print("=" * 60)

x = 100

def demo():
    print(x)

demo()
print(x)


print("\n" + "=" * 60)
print("PROGRAM 57 - Local Variable Shadows Global")
print("=" * 60)

x = 100

def demo():
    x = 200
    print(x)

demo()
print(x)


print("\n" + "=" * 60)
print("PROGRAM 58 - global Keyword")
print("=" * 60)

x = 100

def demo():
    global x
    x = 200

demo()
print(x)


print("\n" + "=" * 60)
print("PROGRAM 59 - len()")
print("=" * 60)

numbers = (10, 20, 30)

print(len(numbers))


print("\n" + "=" * 60)
print("PROGRAM 60 - sum()")
print("=" * 60)

numbers = (10, 20, 30)

print(sum(numbers))


print("\n" + "=" * 60)
print("PROGRAM 61 - max()")
print("=" * 60)

numbers = (10, 20, 30)

print(max(numbers))


print("\n" + "=" * 60)
print("PROGRAM 62 - min()")
print("=" * 60)

numbers = (10, 20, 30)

print(min(numbers))


print("\n" + "=" * 60)
print("PROGRAM 63 - abs()")
print("=" * 60)

print(abs(-100))


print("\n" + "=" * 60)
print("PROGRAM 64 - round()")
print("=" * 60)

print(round(3.14159, 2))


print("\n" + "=" * 60)
print("PROGRAM 65 - sorted()")
print("=" * 60)

numbers = [30, 10, 20]

print(sorted(numbers))


print("\n" + "=" * 60)
print("PROGRAM 66 - Original List")
print("=" * 60)

numbers = [30, 10, 20]

print(numbers)

print("\n")
print("=" * 60)
print("Congratulations! Day09_Programs.py Completed Successfully")
print("=" * 60)