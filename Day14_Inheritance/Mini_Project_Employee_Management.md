# Day 14 Mini Project — Employee Management System

This mini project combines the main Day 14 concepts:

- Inheritance
- Method overriding
- `super()`
- Multiple inheritance
- MRO
- `isinstance()`
- `issubclass()`
- Constructors

## Project Structure

```text
Person
  |
Employee
 /      \
Developer  Tester
 \      /
  TechLead
```

The project keeps the implementation simple enough for Day 14 while demonstrating the OOP concepts we learned.

```python
class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Employee(Person):

    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def display(self):
        super().display()
        print("Employee ID:", self.employee_id)


class Developer(Employee):

    def __init__(self, name, age, employee_id, language):
        super().__init__(name, age, employee_id)
        self.language = language

    def display(self):
        super().display()
        print("Language:", self.language)


class Tester(Employee):

    def __init__(self, name, age, employee_id, tool):
        super().__init__(name, age, employee_id)
        self.tool = tool

    def display(self):
        super().display()
        print("Testing Tool:", self.tool)


class TechLead(Developer, Tester):

    def __init__(self, name, age, employee_id, language, tool):
        # Developer and Tester have different constructor signatures.
        # For this Day 14 project, initialize the common part directly.
        Person.__init__(self, name, age)
        self.employee_id = employee_id
        self.language = language
        self.tool = tool

    def display(self):
        print("----- Tech Lead -----")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.employee_id)
        print("Language:", self.language)
        print("Testing Tool:", self.tool)


# Create objects

developer = Developer(
    "Ravi",
    25,
    101,
    "Python"
)

tester = Tester(
    "Anita",
    28,
    102,
    "Selenium"
)

tech_lead = TechLead(
    "Laxman",
    45,
    103,
    "Python",
    "Selenium"
)


# Display employees

print("DEVELOPER")
developer.display()

print("\nTESTER")
tester.display()

print("\nTECH LEAD")
tech_lead.display()


# Check isinstance()

print("\n--- isinstance() ---")

print(isinstance(developer, Developer))
print(isinstance(developer, Employee))
print(isinstance(developer, Person))

print(isinstance(tech_lead, TechLead))
print(isinstance(tech_lead, Developer))
print(isinstance(tech_lead, Tester))
print(isinstance(tech_lead, Employee))
print(isinstance(tech_lead, Person))


# Check issubclass()

print("\n--- issubclass() ---")

print(issubclass(Developer, Employee))
print(issubclass(Developer, Person))

print(issubclass(TechLead, Developer))
print(issubclass(TechLead, Tester))
print(issubclass(TechLead, Employee))
print(issubclass(TechLead, Person))


# Display MRO

print("\n--- TechLead MRO ---")

print(TechLead.mro())
```

## What This Project Demonstrates

### 1. Inheritance

```text
Developer -> Employee -> Person
Tester -> Employee -> Person
```

### 2. Multiple inheritance

```python
class TechLead(Developer, Tester):
```

### 3. Method overriding

Each child class provides its own `display()` implementation.

### 4. super()

Developer and Tester use:

```python
super().__init__(...)
```

and:

```python
super().display()
```

### 5. MRO

Check:

```python
print(TechLead.mro())
```

The MRO will follow Python's rules for the inheritance hierarchy.

### 6. isinstance()

We check whether an object belongs to a class or one of its parent classes.

### 7. issubclass()

We check whether one class inherits from another.

## Important Design Note

The `TechLead` constructor in this introductory project uses:

```python
Person.__init__(self, name, age)
```

instead of trying to chain `Developer.__init__()` and `Tester.__init__()`.

Why?

Because their constructor signatures are different:

```python
Developer(name, age, employee_id, language)
Tester(name, age, employee_id, tool)
```

A fully cooperative multiple-inheritance design normally gives all classes compatible constructor signatures and uses keyword arguments with `**kwargs`.

That is an advanced improvement and can be learned later.

## Mini Project Questions

Before looking at the answers, try these yourself:

1. What is the MRO of `TechLead`?
2. Is a `TechLead` object an instance of `Developer`?
3. Is a `TechLead` object an instance of `Tester`?
4. Is `Developer` a subclass of `Person`?
5. Why does `Developer.display()` call `super().display()`?
6. Why did we use `Person.__init__()` in `TechLead`?
7. What would happen if `TechLead` did not override `display()`?

## Day 14 Mini Project Goal

The goal is NOT to build a production employee system.

The goal is to make sure you can recognize and use:

```text
Inheritance
      ↓
Method overriding
      ↓
super()
      ↓
Multiple inheritance
      ↓
MRO
      ↓
isinstance()
      ↓
issubclass()
```
