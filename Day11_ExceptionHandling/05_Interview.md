# Day 11 - Exception Handling Interview Questions

---

## 1. What is an Exception?

An Exception is a runtime error that interrupts the normal execution of a program.

---

## 2. What is the difference between a Syntax Error and an Exception?

Syntax Error:
- Occurs before execution.
- Program will not start.

Exception:
- Occurs during execution.
- Can be handled using try-except.

---

## 3. Why do we use Exception Handling?

To prevent the program from terminating unexpectedly and to handle errors gracefully.

---

## 4. What is the purpose of the try block?

The try block contains code that may generate an exception.

---

## 5. What is the purpose of the except block?

It catches and handles the exception.

---

## 6. Can a try block have multiple except blocks?

Yes.

Example:

```python
except ValueError:
    ...

except ZeroDivisionError:
    ...
```

---

## 7. What is Exception as e?

It stores the exception object in a variable.

Example:

```python
except Exception as e:
    print(e)
```

---

## 8. What is the else block?

The else block executes only if no exception occurs.

---

## 9. What is the finally block?

The finally block always executes whether an exception occurs or not.

---

## 10. Why is finally used?

For cleanup activities like:

- Closing files
- Closing database connections
- Releasing resources
- Closing sockets

---

## 11. What is raise?

raise is used to throw an exception manually.

---

## 12. Why do we use raise?

To validate business rules.

Example:

- Invalid Age
- Invalid Salary
- Negative Marks
- Insufficient Balance

---

## 13. What is a Custom Exception?

A user-defined exception created by inheriting from Exception.

---

## 14. Why create Custom Exceptions?

To make code more meaningful and readable.

Example:

- InvalidSalaryError
- InsufficientBalanceError
- InvalidAgeError

---

## 15. Which class should every custom exception inherit from?

Exception

---

## 16. What is pass?

pass is a placeholder statement.

It performs no operation.

---

## 17. Difference between pass, break and continue?

| pass | break | continue |
|------|-------|----------|
| Do Nothing | Exit Loop | Skip Current Iteration |

---

## 18. Name some common built-in exceptions.

- ValueError
- ZeroDivisionError
- IndexError
- KeyError
- TypeError
- FileNotFoundError

---

## 19. What is ValueError?

Raised when a value has the correct type but an invalid value.

---

## 20. What is IndexError?

Raised when accessing an invalid list index.

---

## 21. What is KeyError?

Raised when accessing a missing dictionary key.

---

## 22. What is TypeError?

Raised when an operation is performed on incompatible data types.

---

## 23. What is FileNotFoundError?

Raised when the specified file does not exist.

---

## 24. What happens if an exception is not handled?

The program terminates and displays the traceback.

---

## 25. Can finally execute without except?

Yes.

Example:

```python
try:
    print("Hello")

finally:
    print("Cleanup")
```

---

## 26. Can else exist without except?

No.

---

## 27. Can try exist without except?

Yes, if finally is present.

---

## 28. Is finally always executed?

Yes, in normal program flow.

---

## 29. Is except: recommended?

No.

Prefer:

```python
except ValueError:
```

instead of

```python
except:
```

---

## 30. Why is except: pass bad practice?

Because it hides errors and makes debugging difficult.

---

# Frequently Asked Interview Questions

### Explain the flow of

try → except → else → finally

### Difference between raise and Exception

### Why create Custom Exceptions?

### Give real-world examples of Exception Handling.

### Explain FileNotFoundError.

### Explain ValueError.

### Explain IndexError.

### Explain KeyError.

### Explain TypeError.

### Explain ZeroDivisionError.

---

# Senior Developer Interview Questions

Why should the try block be kept small?

Why should finally be used for cleanup?

How do you design meaningful custom exceptions?

When would you create your own exception instead of using ValueError?

Why should exceptions never be silently ignored?

---

# Day 11 Revision

✔ Exception Basics

✔ try

✔ except

✔ Multiple except

✔ Exception as e

✔ else

✔ finally

✔ raise

✔ pass

✔ Custom Exceptions

✔ Best Practices