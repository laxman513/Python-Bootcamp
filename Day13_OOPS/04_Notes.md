# Day 13 – Object-Oriented Programming (Quick Notes)

---

# 1. Class

A class is a blueprint used to create objects.

Example

class Student:
    pass

---

# 2. Object

An object is an instance of a class.

Example

student = Student()

---

# 3. Constructor

Constructor is a special method that executes automatically whenever an object is created.

Syntax

def __init__(self):
    ...

---

# 4. self

self refers to the current object.

Python passes self automatically.

Java Equivalent

this

---

# 5. Instance Variable

Instance variables belong to individual objects.

Example

self.name = name

Each object has its own copy.

---

# 6. Class Variable

Class variables are shared among all objects.

Example

class Student:

    school = "ABC School"

Only one copy exists.

---

# 7. Instance Method

Uses self.

Can access

- Instance Variables
- Class Variables

Example

def display(self):
    print(self.name)

---

# 8. Class Method

Decorator

@classmethod

Uses

cls

Can modify class variables.

Example

@classmethod
def change_school(cls):
    cls.school = "XYZ"

---

# 9. Static Method

Decorator

@staticmethod

Uses neither self nor cls.

Example

@staticmethod
def add(a,b):
    return a+b

---

# 10. __str__()

Returns object representation.

Example

def __str__(self):
    return self.name

---

# 11. Attribute Lookup

Python searches in this order.

Object

↓

Class

↓

Parent Class

---

# 12. Important Differences

Instance Variable

Different for every object.

Example

self.name

-----------------------------

Class Variable

Common for every object.

Example

Student.school

---

Instance Method

Uses self

Works on Object

---

Class Method

Uses cls

Works on Class

---

Static Method

Uses neither self nor cls

Works as Utility Method

---

# 13. Interview Points

✓ self is NOT a keyword.

✓ cls is NOT a keyword.

✓ __init__() is automatically called.

✓ Every object has separate instance variables.

✓ Class variables are shared.

✓ @classmethod receives class automatically.

✓ @staticmethod receives nothing automatically.

✓ Child object can access parent methods.

✓ Parent object cannot access child methods.

---

# Java Comparison

Python                Java

self              →    this

@classmethod      →    Similar to static

@staticmethod     →    static method

class Dog(Animal) →    class Dog extends Animal

---

# Revision Diagram

Class

↓

Object

↓

Constructor

↓

self

↓

Instance Variables

↓

Instance Methods

↓

Class Variables

↓

Class Methods

↓

Static Methods

↓

Attribute Lookup

↓

Inheritance