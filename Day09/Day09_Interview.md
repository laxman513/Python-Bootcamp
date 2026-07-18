# 📘 Day 09 - Interview Questions
## Topic: Python Functions

---

# Basic Questions

## 1. What is a function?

A function is a reusable block of code that performs a specific task.

---

## 2. Why do we use functions?

- Code Reusability
- Better Readability
- Easy Maintenance
- Avoid Code Duplication
- Easy Testing

---

## 3. What is the syntax of a function?

```python
def function_name():
    pass
```

---

## 4. What is the difference between function definition and function call?

Function Definition

```python
def greet():
    print("Hello")
```

Function Call

```python
greet()
```

Definition creates the function.

Calling executes the function.

---

## 5. What happens if a function is defined but never called?

Nothing happens because Python executes a function only when it is called.

---

# return

## 6. What is return?

`return` sends a value back to the caller.

---

## 7. What is the difference between print() and return()?

| print() | return |
|----------|---------|
| Displays output | Returns a value |
| Cannot be reused | Can be stored and reused |
| Returns None | Returns the specified value |

---

## 8. What does a function return if there is no return statement?

It returns **None**.

---

## 9. Can a function return multiple values?

Yes.

```python
def values():
    return 10,20
```

Python returns them as a tuple.

---

## 10. Can we have multiple return statements?

Yes.

Only one executes depending on the program flow.

---

# Parameters & Arguments

## 11. What is a parameter?

A variable declared in the function definition.

---

## 12. What is an argument?

The actual value passed while calling the function.

---

## 13. Difference between parameter and argument?

| Parameter | Argument |
|------------|----------|
| Variable | Actual Value |
| Function Definition | Function Call |

---

## 14. Is there a limit on the number of parameters?

No.

---

## 15. Can we pass different data types?

Yes.

Python is dynamically typed.

---

# Default Arguments

## 16. What are default arguments?

They provide default values if no argument is supplied.

---

## 17. Can a default value be overridden?

Yes.

---

## 18. Why are default arguments useful?

- Reduce code
- Improve flexibility
- Avoid repeated values

---

# Keyword Arguments

## 19. What are keyword arguments?

Arguments passed using the parameter name.

Example

```python
employee(name="Laxman")
```

---

## 20. Advantages of keyword arguments?

- Readable
- Order independent
- Easy maintenance

---

## 21. Can positional and keyword arguments be mixed?

Yes.

Positional arguments must come first.

Correct

```python
employee("Laxman", city="Hyderabad")
```

Wrong

```python
employee(city="Hyderabad","Laxman")
```

---

# *args

## 22. What is *args?

Accepts any number of positional arguments.

---

## 23. What data type is *args?

Tuple.

---

## 24. Can *args be empty?

Yes.

---

## 25. Why use *args?

When the number of arguments is unknown.

---

# **kwargs

## 26. What is **kwargs?

Accepts any number of keyword arguments.

---

## 27. What data type is **kwargs?

Dictionary.

---

## 28. Difference between *args and **kwargs?

| *args | **kwargs |
|--------|-----------|
| Tuple | Dictionary |
| Positional | Keyword |

---

# Scope

## 29. What is a local variable?

Declared inside a function.

Accessible only inside that function.

---

## 30. What is a global variable?

Declared outside a function.

Accessible throughout the program.

---

## 31. What is the global keyword?

It allows a function to modify a global variable.

---

## 32. Can a local variable have the same name as a global variable?

Yes.

The local variable hides (shadows) the global variable inside that function.

---

# Built-in Functions

## 33. What does len() do?

Returns the number of items.

---

## 34. What does sum() do?

Returns the sum of numeric values.

---

## 35. What does max() do?

Returns the largest value.

---

## 36. What does min() do?

Returns the smallest value.

---

## 37. What does abs() do?

Returns the absolute (positive) value.

---

## 38. What does round() do?

Rounds a floating-point number.

Example

```python
round(3.14159, 2)
```

Output

```
3.14
```

---

## 39. Difference between sorted() and list.sort()?

| sorted() | list.sort() |
|-----------|-------------|
| Returns a new list | Modifies the original list |
| Works on many iterables | Only for lists |

---

## 40. Name five commonly used built-in functions.

- len()
- sum()
- max()
- min()
- sorted()

---

# Java Interview Comparison

Java

```java
public static int add(int a,int b)
```

Python

```python
def add(a,b):
    return a+b
```

Python does not require:

- public
- private
- static
- return type
- braces `{}`

---

# Frequently Asked Interview Questions

- What is recursion?
- What are lambda functions?
- What are decorators?
- What are generators?
- What is variable scope?
- What is the LEGB rule?
- What is the difference between global and nonlocal?
- What is the difference between mutable and immutable objects?

> **Note:** We will cover these topics in upcoming days.

---

# Day 09 Quick Revision

✔ Functions

✔ return

✔ pass

✔ Parameters

✔ Arguments

✔ Default Arguments

✔ Keyword Arguments

✔ Positional Arguments

✔ *args

✔ **kwargs

✔ Local Variables

✔ Global Variables

✔ global Keyword

✔ Built-in Functions

---

# Interview Tip

Functions are one of the most frequently asked Python topics. Be comfortable writing small functions without looking at notes.