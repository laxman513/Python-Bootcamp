# ==========================================================
# Day 08 - Python Sets
# Author: Laxman
# Bootcamp Day: 08
# ==========================================================

print("=" * 60)
print("PROGRAM 1 - Creating a Set")
print("=" * 60)

numbers = {10, 20, 30}
print(numbers)
print(type(numbers))


print("\n" + "=" * 60)
print("PROGRAM 2 - Duplicate Elements")
print("=" * 60)

numbers = {10, 20, 20, 30, 30, 40}
print(numbers)
print(len(numbers))


print("\n" + "=" * 60)
print("PROGRAM 3 - Membership Operator")
print("=" * 60)

letters = {"A", "B", "C"}

print("A" in letters)
print("D" in letters)


print("\n" + "=" * 60)
print("PROGRAM 4 - Empty Curly Braces")
print("=" * 60)

numbers = {}

print(type(numbers))


print("\n" + "=" * 60)
print("PROGRAM 5 - Empty Set")
print("=" * 60)

numbers = set()

print(type(numbers))


print("\n" + "=" * 60)
print("PROGRAM 6 - add()")
print("=" * 60)

numbers = {10, 20}

numbers.add(30)

print(numbers)


print("\n" + "=" * 60)
print("PROGRAM 7 - remove()")
print("=" * 60)

numbers = {10, 20, 30}

numbers.remove(20)

print(numbers)


print("\n" + "=" * 60)
print("PROGRAM 8 - remove() with Non-existing Element")
print("=" * 60)

numbers = {10, 20}

try:
    numbers.remove(100)
except KeyError as e:
    print("Error:", e)


print("\n" + "=" * 60)
print("PROGRAM 9 - discard()")
print("=" * 60)

numbers = {10, 20}

numbers.discard(100)

print(numbers)


print("\n" + "=" * 60)
print("PROGRAM 10 - clear()")
print("=" * 60)

numbers = {10, 20, 30}

numbers.clear()

print(numbers)
print(len(numbers))


print("\n" + "=" * 60)
print("PROGRAM 11 - update()")
print("=" * 60)

numbers = {10, 20}

numbers.update([30, 40])

print(numbers)


print("\n" + "=" * 60)
print("PROGRAM 12 - Union")
print("=" * 60)

a = {1, 2, 3}
b = {3, 4, 5}

print(a | b)


print("\n" + "=" * 60)
print("PROGRAM 13 - Intersection")
print("=" * 60)

a = {1, 2, 3}
b = {3, 4, 5}

print(a & b)


print("\n" + "=" * 60)
print("PROGRAM 14 - Difference")
print("=" * 60)

a = {1, 2, 3}
b = {3, 4, 5}

print(a - b)


print("\n" + "=" * 60)
print("MINI PROJECT - Student Course Management")
print("=" * 60)

students_python = {"Laxman", "Rahul", "Amit"}
students_java = {"Laxman", "Priya", "Amit"}

print("All Unique Students")
print("-------------------")
print(students_python | students_java)

print("\nStudents Enrolled in Both Courses")
print("---------------------------------")
print(students_python & students_java)

print("\nStudents Only in Python")
print("-----------------------")
print(students_python - students_java)

print("\nAdding Kiran")
students_python.add("Kiran")

print("Removing Rahul")
students_python.remove("Rahul")

print("\nFinal Python Students")
print("---------------------")
print(students_python)


print("\n" + "=" * 60)
print("BONUS PROGRAM - Mutable vs Immutable")
print("=" * 60)

print("Mutable Types")
print("list")
print("dict")
print("set")

print()

print("Immutable Types")
print("int")
print("float")
print("bool")
print("str")
print("tuple")