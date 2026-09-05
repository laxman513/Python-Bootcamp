# Program 13 — Handling Multiple File Exceptions

## Objective

Learn how to handle different exceptions using multiple `except` blocks.

## Concepts

- try
- except
- FileNotFoundError
- PermissionError
- Multiple exception handlers

## Structure

try:
    # File operation

except FileNotFoundError:
    # File doesn't exist

except PermissionError:
    # Permission problem

## Why?

Different problems require different messages.

For example:

FileNotFoundError
→ File doesn't exist.

PermissionError
→ We don't have permission to access the file.

## Expected Output

Because missing.txt does not exist, the program should display:

File not found: missing.txt

## Checklist

- [ ] Created 13_multiple_file_exceptions.py
- [ ] Created 13_multiple_file_exceptions.md
- [ ] Used multiple except blocks
- [ ] Ran the program
- [ ] Verified the output