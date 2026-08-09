# Day 14 — Interview Questions

## 1. What is inheritance?
Inheritance allows a child class to reuse properties and methods of a parent class.

## 2. What is method overriding?
When a child class provides its own implementation of a parent method.

## 3. What is super()?
`super()` continues method/attribute lookup according to the MRO.

## 4. Does super() always call the immediate parent?
No. It follows MRO. In multiple inheritance it can call another class in the MRO.

## 5. Does Python support multiple inheritance?
Yes.

```python
class Child(Father, Mother):
    pass
```

## 6. What is MRO?
Method Resolution Order: the order Python uses to search classes for methods and attributes.

## 7. How can you see MRO?
```python
print(ClassName.mro())
print(ClassName.__mro__)
```

## 8. What is diamond inheritance?
A structure where two classes share a common parent and another class inherits from both.

```text
    A
   / \
  B   C
   \ /
    D
```

## 9. How does Python solve the diamond problem?
Using MRO based on C3 Linearization.

## 10. What is cooperative multiple inheritance?
Classes consistently use `super()` so every class in the MRO can participate.

## 11. What is isinstance()?
Checks whether an object is an instance of a class.

## 12. What is issubclass()?
Checks whether one class is derived from another.

## 13. Why use super().__init__()?
To continue constructor initialization through the MRO.

## 14. Why is parent order important?
Because it changes the MRO and therefore method lookup.

## 15. What is the key Day 14 rule?
```text
super() -> follows MRO
```

Not:
```text
super() -> always calls immediate parent
```

## 16. Explain Program 35.

For:

```python
class D(B, C):
    ...
```

the MRO is:

```text
D -> B -> C -> A -> object
```

Therefore:

```text
D.super() -> B
B.super() -> C
C.super() -> A
```

Because each method prints after `super()`, the final output is:

```text
A
C
B
D
```
