# Day 10 - Modules & Packages

## Topics Covered

- Built-in Modules
- math Module
- random Module
- datetime Module
- Creating Custom Modules
- Different Import Methods
- Module Alias
- __name__
- __main__
- Packages
- __init__.py
- Module Search Path (sys.path)

---

## Built-in Modules

Python provides many built-in modules.

Examples:

- math
- random
- datetime
- os
- sys
- time

Import Example

```python
import math

print(math.sqrt(25))
```

---

## Different Import Methods

### Import Entire Module

```python
import math

print(math.sqrt(25))
```

---

### Import Specific Function

```python
from math import sqrt

print(sqrt(25))
```

---

### Import with Alias

```python
import math as mt

print(mt.factorial(5))
```

---

## Random Module

```python
import random

print(random.randint(1,100))
```

---

## Datetime Module

```python
import datetime

print(datetime.date.today())

now = datetime.datetime.now()

print(now.year)
print(now.month)
print(now.day)
```

---

## Creating Custom Module

calculator.py

```python
def add(a,b):
    return a+b
```

main.py

```python
import calculator

print(calculator.add(10,20))
```

---

## __name__

Every Python file has a built-in variable.

```python
print(__name__)
```

If executed directly

```
__main__
```

If imported

```
Module Name
```

---

## __main__

```python
if __name__=="__main__":
    print("Testing")
```

Purpose:

Execute code only when the file is run directly.

---

## Packages

A package is a collection of related modules.

Example

```
employee/

    __init__.py

    salary.py

    attendance.py
```

Import

```python
from employee.salary import calculate
```

---

## __init__.py

Used for package initialization.

Modern Python (3.3+) does not require it, but it is still widely used in professional projects.

---

## sys.path

Python searches modules from locations stored in

```python
import sys

print(sys.path)
```

---

## Best Practices

✔ Keep one responsibility per module.

✔ Use packages for large applications.

✔ Avoid using

```python
from module import *
```

unless necessary.

✔ Use

```python
if __name__=="__main__":
```

for testing.

---

## Summary

Today we learned

- Built-in Modules
- Custom Modules
- Import Styles
- datetime
- random
- math
- Packages
- __name__
- __main__
- sys.path

These concepts are used in almost every real-world Python application.