# ============================================================
# Day 09 Assignments - Python Functions
# Author : Laxman
# ============================================================

print("=" * 60)
print("DAY 09 ASSIGNMENTS - SOLUTIONS")
print("=" * 60)

# ============================================================
# Assignment 1
# ============================================================

# Question:
# Write a function to print "Welcome to Python".

def welcome():
    print("Welcome to Python")

welcome()


# ============================================================
# Assignment 2
# ============================================================

# Question:
# Write a function that accepts a name and prints:
# Hello <name>

def greet(name):
    print("Hello", name)

greet("Laxman")


# ============================================================
# Assignment 3
# ============================================================

# Question:
# Write a function to add two numbers and return the result.

def add(a, b):
    return a + b

result = add(10, 20)
print("Sum =", result)


# ============================================================
# Assignment 4
# ============================================================

# Question:
# Write a function to find the biggest of two numbers.

def biggest(a, b):
    if a > b:
        return a
    else:
        return b

print("Biggest =", biggest(25, 40))


# ============================================================
# Assignment 5
# ============================================================

# Question:
# Write a function to calculate the square of a number.

def square(number):
    return number * number

print("Square =", square(12))

print("\nAssignments 1 - 5 Completed")

# ============================================================
# Assignment 6
# ============================================================

# Question:
# Write a function with default parameter.
#
# Example:
# greet()
# Hello Guest
#
# greet("Laxman")
# Hello Laxman

def greet(name="Guest"):
    print("Hello", name)

greet()
greet("Laxman")


# ============================================================
# Assignment 7
# ============================================================

# Question:
# Write a function that accepts
# Name
# Age
# City
#
# Print all details.

def employee(name, age, city):
    print("Employee Details")
    print("-" * 25)
    print("Name :", name)
    print("Age  :", age)
    print("City :", city)

employee("Laxman", 46, "Hyderabad")


# ============================================================
# Assignment 8
# ============================================================

# Question:
# Write a function using *args
#
# Accept any number of integers
# Return their sum.

def add_numbers(*numbers):
    return sum(numbers)

print("Sum =", add_numbers(10, 20, 30))
print("Sum =", add_numbers(5, 10, 15, 20, 25))


# ============================================================
# Assignment 9
# ============================================================

# Question:
# Write a function using **kwargs
#
# Print all employee details.

def employee_details(**kwargs):

    print("Employee Details")
    print("-" * 30)

    for key, value in kwargs.items():
        print(f"{key} : {value}")

employee_details(
    name="Laxman",
    age=46,
    city="Hyderabad",
    company="JPMC"
)


# ============================================================
# Assignment 10
# ============================================================

# Question:
# Write a function to find
# Maximum number using max()

def find_max(*numbers):
    return max(numbers)

print("Maximum =", find_max(10, 50, 25, 80, 40))

print("\nAssignments 6 - 10 Completed")

# ============================================================
# Assignment 11
# ============================================================

# Question:
# Write a function to return
# Minimum number using min()

def find_min(*numbers):
    return min(numbers)

print("Minimum =", find_min(10, 50, 25, 80, 40))


# ============================================================
# Assignment 12
# ============================================================

# Question:
# Write a function to reverse a string.

def reverse_string(text):
    return text[::-1]

print("Reversed String =", reverse_string("Python"))


# ============================================================
# Assignment 13
# ============================================================

# Question:
# Write a function to count vowels
# in a string.

def count_vowels(text):

    vowels = "aeiouAEIOU"
    count = 0

    for ch in text:
        if ch in vowels:
            count += 1

    return count

word = "Hyderabad"

print("Word          :", word)
print("Vowel Count   :", count_vowels(word))


# ============================================================
# Assignment 14
# ============================================================

# Question:
# Write a function to check
# whether a number is even or odd.

def check_even_odd(number):

    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"

print("25 is", check_even_odd(25))
print("100 is", check_even_odd(100))


# ============================================================
# Assignment 15
# ============================================================

# Question:
# Write a function that accepts
# a list and returns the largest element.

def largest_element(numbers):
    return max(numbers)

my_list = [25, 80, 10, 95, 45]

print("List            :", my_list)
print("Largest Element :", largest_element(my_list))


# ============================================================
# MINI CHALLENGE
# ============================================================

# Create one function named employee()
#
# It should support:
#
# employee(
#     name="Laxman",
#     age=46,
#     city="Hyderabad",
#     company="JPMC"
# )
#
# Print every key and value neatly.

def employee(**kwargs):

    print("\nEmployee Details")
    print("-" * 35)

    for key, value in kwargs.items():
        print(f"{key:<10} : {value}")

employee(
    name="Laxman",
    age=46,
    city="Hyderabad",
    company="JPMC"
)

print("\n")
print("=" * 60)
print("Congratulations! Day09_Assignments.py Completed Successfully")
print("=" * 60)