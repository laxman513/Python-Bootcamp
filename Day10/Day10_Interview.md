# Day 10 Interview Questions

## Basic

### 1. What is a module?

A module is a Python (.py) file containing functions, variables, classes, and reusable code.

---

### 2. What is a package?

A package is a collection of related Python modules.

---

### 3. Difference between module and package?

Module → Single Python file.

Package → Folder containing multiple related modules.

---

### 4. Name some built-in modules.

- math
- random
- datetime
- os
- sys
- time

---

### 5. Difference between

```python
import math
```

and

```python
from math import sqrt
```

The first imports the complete module.

The second imports only the specified function.

---

### 6. Why use aliases?

Example

```python
import math as mt
```

Used to shorten long module names and improve readability.

---

### 7. What is __name__?

It is a built-in variable that stores the current module name.

---

### 8. What is __main__?

It is the value assigned to __name__ when the file is executed directly.

---

### 9. Why use

```python
if __name__=="__main__":
```

To prevent test code from running when the module is imported.

---

### 10. What is __init__.py?

It initializes a package.

Although optional in modern Python, it is commonly used.

---

### 11. Is __init__.py mandatory?

No.

Since Python 3.3, it is optional.

---

### 12. What is sys.path?

It stores the list of directories Python searches for modules.

---

### 13. Difference between random.randint() and random.choice()

randint()

Returns a random integer.

choice()

Returns a random element from a sequence.

---

### 14. Difference between datetime.date and datetime.datetime

date

Stores only the date.

datetime

Stores both date and time.

---

### 15. Why create your own modules?

To improve code reuse, readability, maintainability, and organization.

---

## Frequently Asked Interview Questions

✔ What is a Python module?

✔ What is a package?

✔ Explain __name__.

✔ Explain __main__.

✔ Different import methods.

✔ Difference between package and module.

✔ Explain alias import.

✔ Explain built-in modules.

✔ Explain sys.path.

✔ Explain __init__.py.