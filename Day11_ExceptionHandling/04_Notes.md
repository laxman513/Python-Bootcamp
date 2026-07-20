# Day 11 - Exception Handling

---

# What is an Exception?

An Exception is a runtime error that interrupts the normal flow of program execution.

Examples:

- ZeroDivisionError
- ValueError
- TypeError
- IndexError
- KeyError
- FileNotFoundError

---

# Syntax Error vs Runtime Error

Syntax Error

- Occurs before execution.
- Program does not start.
- Example:

```python
if True
    print("Hello")
```

Runtime Error (Exception)

- Occurs while the program is running.

Example:

```python
print(10 / 0)
```

---

# try

The risky code is placed inside the try block.

```python
try:
    print(10 / 2)
```

---

# except

Handles the exception.

```python
try:
    print(10 / 0)

except ZeroDivisionError:
    print("Cannot divide by zero.")
```

---

# Multiple except Blocks

```python
try:
    number = int(input())

    print(100 / number)

except ValueError:
    print("Invalid Number")

except ZeroDivisionError:
    print("Cannot divide by zero")
```

---

# Generic Exception

```python
try:

    print(10 / 0)

except Exception as e:

    print(e)
```

Useful when the exact exception type is unknown.

---

# else

Executed only when no exception occurs.

```python
try:

    print(10 / 2)

except ZeroDivisionError:

    print("Error")

else:

    print("Success")
```

---

# finally

Always executes whether an exception occurs or not.

```python
try:

    print(10 / 2)

finally:

    print("Cleanup")
```

Used for:

- Closing files
- Closing database connections
- Releasing resources
- Closing sockets

---

# raise

Used to throw an exception manually.

```python
age = -5

if age < 0:

    raise ValueError("Age cannot be negative")
```

---

# Custom Exception

```python
class InvalidAgeError(Exception):
    pass
```

Raise it

```python
raise InvalidAgeError("Invalid Age")
```

---

# pass

pass is a placeholder statement.

It does nothing.

Useful for:

- Empty Classes
- Empty Functions
- Future implementation

Example

```python
class Employee:
    pass
```

---

# Common Built-in Exceptions

| Exception | Reason |
|-----------|----------------------------|
| ValueError | Invalid value |
| ZeroDivisionError | Divide by zero |
| IndexError | Invalid list index |
| KeyError | Invalid dictionary key |
| TypeError | Unsupported data types |
| FileNotFoundError | File does not exist |

---

# Best Practices

✅ Catch specific exceptions.

```python
except ValueError:
```

Instead of

```python
except Exception:
```

unless needed.

---

Keep the try block as small as possible.

---

Use finally for cleanup.

---

Raise meaningful exceptions.

---

Never write

```python
except:
    pass
```

because it hides errors.

---

# Interview Tips

Difference between

pass

break

continue

| pass | break | continue |
|------|-------|----------|
| Do nothing | Exit loop | Skip current iteration |

---

# Java vs Python

Java

```java
class MyException extends Exception{

}
```

Python

```python
class MyException(Exception):
    pass
```

---

# Day 11 Summary

Topics Covered

- Exception Basics
- try
- except
- Multiple except
- Exception as e
- else
- finally
- raise
- Custom Exceptions
- pass
- Best Practices

---

# Real World Usage

- Banking Applications
- ATM Systems
- File Processing
- Database Connections
- API Calls
- Payment Gateways
- Web Applications

---

# Quick Revision

Remember

try

↓

except

↓

else

↓

finally

raise → Throw Exception

pass → Do Nothing

Exception → Runtime Error

Custom Exception → User-defined Exception