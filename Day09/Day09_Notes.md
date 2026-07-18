# 📘 Day 09 - Python Functions

## 🎯 Learning Objectives

Today we learned:

- What is a Function?
- Why Functions are used?
- Function Definition
- Function Calling
- return Statement
- pass Statement
- Parameters
- Arguments
- Default Parameters
- Keyword Arguments
- Positional Arguments
- *args
- **kwargs
- Local Variables
- Global Variables
- global Keyword
- Built-in Functions

---

# 1. What is a Function?

A function is a block of reusable code that performs a specific task.

Instead of writing the same code multiple times, we write it once and call it whenever required.

Example:

```python
def greet():
    print("Hello")

greet()
```

---

# 2. Advantages of Functions

- Code Reusability
- Easy Maintenance
- Better Readability
- Reduces Duplicate Code
- Easy Testing

---

# 3. Function Syntax

```python
def function_name():
    statements
```

Example

```python
def greet():
    print("Hello")
```

Calling

```python
greet()
```

---

# 4. Function Definition vs Function Call

Definition

```python
def greet():
    print("Hello")
```

Calling

```python
greet()
```

Definition only creates the function.

Calling executes it.

---

# 5. pass Statement

Sometimes we don't want to write code immediately.

```python
def greet():
    pass
```

Python allows an empty function only because of `pass`.

---

# 6. return Statement

`return` sends a value back to the caller.

Example

```python
def add():
    return 30
```

```
print(add())
```

Output

```
30
```

---

# print() vs return

print()

- Displays output
- Doesn't return useful data

return

- Sends value back
- Can be stored in a variable
- Can be reused

Example

```python
result = add()
```

---

# 7. Parameters

Parameters are variables declared in the function definition.

```python
def greet(name):
```

"name" is the parameter.

---

# 8. Arguments

Arguments are actual values passed while calling.

```python
greet("Laxman")
```

"Laxman" is the argument.

---

# 9. Default Parameters

```python
def greet(name="Guest"):
```

If no value is passed,

Guest will be used.

---

# 10. Keyword Arguments

```python
employee(name="Laxman", city="Hyderabad")
```

Advantages

- Better readability
- Order doesn't matter

---

# 11. Positional Arguments

Arguments are assigned according to position.

```python
add(10,20)
```

10 → first parameter

20 → second parameter

---

# 12. *args

Used when number of arguments is unknown.

```python
def add(*args):
```

args is stored as a Tuple.

Example

```python
add(10)
add(10,20)
add(10,20,30)
```

---

# 13. **kwargs

Used when unknown keyword arguments are passed.

```python
def employee(**kwargs):
```

Stored as Dictionary.

Example

```python
employee(name="Laxman", age=46)
```

---

# *args vs **kwargs

| *args | **kwargs |
|--------|-----------|
| Tuple | Dictionary |
| Positional | Keyword |
| * | ** |

---

# 14. Local Variable

Created inside function.

Accessible only inside that function.

```python
def demo():
    x=10
```

Outside the function

```
Error
```

---

# 15. Global Variable

Declared outside the function.

Accessible everywhere.

```python
city="Hyderabad"
```

---

# 16. global Keyword

Allows modifying a global variable.

Example

```python
x=100

def demo():
    global x
    x=200
```

---

# 17. Built-in Functions

Python already provides many useful functions.

Examples

```
print()
len()
sum()
max()
min()
round()
abs()
type()
sorted()
```

---

# sorted() vs sort()

sorted()

- Returns a NEW list
- Original list unchanged

sort()

- Changes original list
- Returns None

---

# Common Errors

NameError

```python
print(message)
```

Outside scope.

TypeError

Wrong arguments.

IndexError

Invalid index.

KeyError

Invalid dictionary key.

---

# Java vs Python

Java

```java
public static int add(int a,int b)
```

Python

```python
def add(a,b):
```

No

- public
- private
- static
- return type
- braces

Required in Python.

---

# Best Practices

✔ Use meaningful function names

✔ Keep functions short

✔ Return values instead of printing

✔ Avoid unnecessary global variables

✔ Use keyword arguments when readability matters

---

# AI / GenAI Relevance

Functions are used everywhere in AI.

Examples

- Data preprocessing
- Model training
- Prediction
- API development
- RAG pipelines
- LangChain tools
- FastAPI endpoints

Without functions, large AI applications become difficult to maintain.

---

# Day 09 Summary

Today you learned the complete fundamentals of Python Functions.

This is one of the most important topics because every Python project—from automation scripts to AI applications—uses functions extensively.