# Day 16 - Polymorphism & Abstraction

## 1. Polymorphism

Polymorphism means one interface/operation can work with different objects.

Example:

```python
for payment in payments:
    payment.pay()
```

Each object can provide different behavior.

## 2. Method Overriding

A child class provides its own implementation of a parent method.

```python
class Parent:
    def show(self):
        print("Parent")

class Child(Parent):
    def show(self):
        print("Child")
```

## 3. super()

`super()` allows the child to call the parent implementation.

```python
super().pay()
```

## 4. Duck Typing

Python focuses on what an object can do rather than its exact class.

If an object has:

```python
obj.pay()
```

it can be used by code that expects something with `pay()`.

## 5. Built-in Polymorphism

`len()`, `+`, `*`, and `sorted()` behave differently depending on the object.

```python
len("Python")
len([1, 2, 3])
```

## 6. sorted() and key

```python
sorted(employees, key=lambda employee: employee.salary)
```

`key` tells Python which value to use for sorting.

## 7. Functions as Arguments

Functions are first-class objects.

```python
calculate(square, 5)
```

The function `square` is passed without `()`.

## 8. Abstract Classes

```python
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self):
        pass
```

An abstract class acts as a blueprint/contract.

A class containing unimplemented abstract methods cannot normally be instantiated.

## 9. Abstract Methods

```python
@abstractmethod
def pay(self):
    pass
```

A concrete child class must implement the abstract method.

## 10. Abstract Properties

```python
@property
@abstractmethod
def salary(self):
    pass
```

The child must implement the property.

Access:

```python
employee.salary
```

not:

```python
employee.salary()
```

## 11. Property vs Method

Property:

```python
employee.salary
```

Normal method:

```python
payment.process()
```

Golden rule:

**@property -> no parentheses**

**normal method -> parentheses**

## 12. Main Day 16 Combination

Day 16 combines:

- Inheritance
- Method overriding
- Polymorphism
- Duck typing
- Abstract classes
- Abstract methods
- Abstract properties
- Functions as arguments
- `sorted(key=...)`

These concepts are very important for Java/Python OOP interviews.
