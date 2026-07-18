# Day 08 - Python Sets

## Status

✅ Completed

---

# Learning Objectives

By the end of Day 8, you should be able to:

- Create sets
- Understand duplicate removal
- Differentiate between list, tuple, dict and set
- Use set methods
- Perform union, intersection and difference
- Understand mutable vs immutable objects

---

# What is a Set?

A set is an unordered collection of unique elements.

Example:

```python
numbers = {10, 20, 30}
```

Properties:

- Unordered
- Mutable
- No duplicate values
- No indexing

---

# Creating Sets

```python
numbers = {10,20,30}
```

Empty set:

```python
numbers = set()
```

⚠️

```python
{}
```

creates an empty dictionary, NOT a set.

---

# Membership

```python
"A" in letters
```

Returns:

```python
True
```

or

```python
False
```

---

# Set Methods

## add()

Adds one element.

```python
numbers.add(40)
```

---

## update()

Adds multiple elements.

```python
numbers.update([50,60])
```

Important:

```python
numbers.update("Python")
```

adds

P

y

t

h

o

n

individually because strings are iterable.

To add one string:

```python
numbers.add("Python")
```

---

## remove()

Removes an element.

Raises

```
KeyError
```

if the element doesn't exist.

---

## discard()

Removes an element.

Does NOT raise an error if the element doesn't exist.

---

## clear()

Removes every element.

---

# Set Operations

## Union

```python
a | b
```

Returns all unique elements.

---

## Intersection

```python
a & b
```

Returns common elements.

---

## Difference

```python
a - b
```

Returns elements present in first set only.

---

# Mutable vs Immutable

## Mutable

- list
- dict
- set

These objects can be modified after creation.

---

## Immutable

- int
- float
- bool
- str
- tuple

These cannot be modified after creation.

---

# Java vs Python

Java

```java
HashSet<String> set = new HashSet<>();
```

Python

```python
numbers = set()
```

No `new` keyword.

---

# Common Mistakes

❌

```python
{}
```

is NOT a set.

---

❌

```python
numbers.update("Kiran")
```

Adds every character individually.

Use

```python
numbers.add("Kiran")
```

instead.

---

# Interview Tips

✔ Difference between remove() and discard()

✔ Mutable vs Immutable

✔ Why {} creates dict

✔ Set vs List

✔ Set operations

---

# Summary

Today you learned:

- Sets
- Duplicate removal
- Membership
- add()
- update()
- remove()
- discard()
- clear()
- Union
- Intersection
- Difference
- Mutable vs Immutable