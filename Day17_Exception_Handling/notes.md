# Day 17 — Python Exception Handling Notes

## Core concepts
- Exception: a runtime event that interrupts normal execution.
- `try`: code that may raise an exception.
- `except`: handles a matching exception.
- `else`: runs only when the `try` block succeeds without an exception.
- `finally`: cleanup block; runs whether an exception occurs or not.
- `raise`: manually raises an exception.
- Custom exception: an application-specific exception class, normally inheriting from `Exception`.

## Common exceptions
- `ValueError` — invalid value
- `TypeError` — incompatible type operation
- `ZeroDivisionError` — division by zero
- `IndexError` — invalid sequence index
- `KeyError` — missing dictionary key
- `FileNotFoundError` — requested file does not exist

## Correct block order
`try -> except -> else -> finally`

`else` must come before `finally`.

## Exception object
```python
except ValueError as error:
    print(error)
```

## Custom exception
```python
class InsufficientBalanceError(Exception):
    pass
```

## Best practices
1. Prefer specific exceptions.
2. Put specific handlers before `except Exception`.
3. Use meaningful messages.
4. Do not silently ignore exceptions.
5. Use `with` for file/resource handling when possible.
6. Use custom exceptions for important business rules.
