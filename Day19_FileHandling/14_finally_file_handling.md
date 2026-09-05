# Program 14 — finally with File Handling

## Objective

Learn how `finally` works when handling files.

## Concepts

- try
- except
- finally
- FileNotFoundError
- Cleanup code

## Important Point

The `finally` block executes whether an exception occurs or not.

Structure:

try:
    # risky operation

except:
    # handle error

finally:
    # always executes

## Program

The program attempts to open a file that does not exist.

The exception is handled, and finally executes.

## Expected Output

File not found.
Finally block executed.

## Why is finally useful?

It is commonly used for cleanup operations.

For example:

- closing resources
- releasing connections
- cleaning temporary resources

With `with open()`, Python normally handles file closing automatically, so
we don't normally need finally just to close a file.

## Checklist

- [ ] Created 14_finally_file_handling.py
- [ ] Created 14_finally_file_handling.md
- [ ] Used try
- [ ] Used except
- [ ] Used finally
- [ ] Verified finally executes