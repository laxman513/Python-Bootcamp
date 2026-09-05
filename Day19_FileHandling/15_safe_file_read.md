# Program 15 — Safe File Reading Function

## Objective

Create a reusable function that safely reads a file.

## Concepts

- Functions
- Parameters
- return
- with open()
- FileNotFoundError
- Exception handling

## Problem

Suppose an application needs to read many different files.

Instead of writing:

try:
    with open(...)
    ...
except FileNotFoundError:
    ...

every time, we can create a reusable function.

## Function

read_file(filename)

The function:

1. Receives a filename.
2. Opens the file.
3. Reads the contents.
4. Returns the contents.
5. Handles FileNotFoundError.

## Expected Output

The existing context_output.txt should be displayed.

For a missing file, a friendly message should be displayed.

## Checklist

- [ ] Created 15_safe_file_read.py
- [ ] Created 15_safe_file_read.md
- [ ] Created a reusable function
- [ ] Used FileNotFoundError
- [ ] Tested existing file
- [ ] Tested missing file