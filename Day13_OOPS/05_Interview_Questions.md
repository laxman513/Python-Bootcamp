# Day 13 – Interview Questions

## Basic Questions

### 1. What is a class?

A class is a blueprint used to create objects.

---

### 2. What is an object?

An object is an instance of a class.

---

### 3. What is OOP?

Object-Oriented Programming (OOP) is a programming paradigm based on classes and objects.

---

### 4. What are the four pillars of OOP?

- Inheritance
- Polymorphism
- Encapsulation
- Abstraction

---

### 5. What is __init__()?

__init__() is a special method (constructor) that executes automatically whenever an object is created.

---

### 6. Is __init__() automatically called?

Yes.

---

### 7. What is self?

self refers to the current object.

---

### 8. Is self a keyword?

No.

It is only a convention.

---

### 9. Who passes self?

Python automatically passes self.

---

### 10. Java equivalent of self?

this

---

## Instance Variables

### 11. What is an instance variable?

Instance variables belong to individual objects.

Example

```python
self.name = name
```

---

### 12. Where are instance variables stored?

Inside each object.

---

### 13. Can two objects have different instance variable values?

Yes.

---

## Class Variables

### 14. What is a class variable?

Class variables are shared among all objects.

Example

```python
company = "JP Morgan"
```

---

### 15. How many copies of a class variable exist?

Only one.

---

### 16. How do you modify a class variable?

```python
Employee.company = "Google"
```

or

```python
@classmethod
def change_company(cls):
    cls.company = "Google"
```

---

## Instance Methods

### 17. What is an instance method?

A method that works on object data.

Uses

```python
self
```

---

### 18. Can instance methods access class variables?

Yes.

---

## Class Methods

### 19. What is a class method?

A method that works on class variables.

Decorator

```python
@classmethod
```

---

### 20. What is cls?

cls refers to the current class.

---

### 21. Is cls a keyword?

No.

It is only a convention.

---

### 22. Can we use another name instead of cls?

Yes.

But cls is the recommended convention.

---

### 23. Can a class method modify class variables?

Yes.

---

## Static Methods

### 24. What is a static method?

A method that belongs to the class but doesn't use object or class data.

---

### 25. Which decorator is used?

```python
@staticmethod
```

---

### 26. Does a static method receive self?

No.

---

### 27. Does a static method receive cls?

No.

---

### 28. Java equivalent of static method?

static method

---

## Attribute Lookup

### 29. Explain Attribute Lookup.

Python searches in this order

Object

↓

Class

↓

Parent Class

---

### 30. What happens if an object has its own variable?

Python uses the instance variable.

---

### 31. What happens if instance variable is not found?

Python searches the class.

---

## __str__()

### 32. What is __str__()?

Returns the string representation of an object.

---

## Coding Questions

### 33. Difference between instance variable and class variable.

| Instance Variable | Class Variable |
|-------------------|----------------|
| Belongs to object | Belongs to class |
| Different for every object | Shared by all objects |
| Uses self | Uses class name or cls |

---

### 34. Difference between instance method, class method and static method.

| Instance | Class | Static |
|----------|-------|--------|
| self | cls | No parameter |
| Object | Class | Utility |
| Uses object data | Uses class data | Uses neither |

---

### 35. Difference between self and cls.

| self | cls |
|------|------|
| Current Object | Current Class |
| Instance Method | Class Method |

---

## Interview Tips

✅ self is not a keyword.

✅ cls is not a keyword.

✅ Every object has separate instance variables.

✅ Class variables are shared.

✅ @classmethod receives class automatically.

✅ @staticmethod receives nothing automatically.

✅ Python uses Attribute Lookup.

Object

↓

Class

↓

Parent Class

---

## Java Comparison

| Python | Java |
|---------|------|
| self | this |
| @classmethod | Similar to static (receives cls) |
| @staticmethod | static method |
| class Dog(Animal) | class Dog extends Animal |

---

# Revision Checklist

✅ Class

✅ Object

✅ Constructor

✅ self

✅ Instance Variable

✅ Instance Method

✅ Class Variable

✅ Class Method

✅ Static Method

✅ __str__()

✅ Attribute Lookup