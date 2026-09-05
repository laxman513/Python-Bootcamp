# Program 8 — Using with open() for Appending

## Objective

Learn how to append data to an existing file using the `with open()` context manager.

## Concepts

- `with open()`
- Append mode `"a"`
- Adding data without deleting existing content
- Automatic file closing

## Code

with open("context_output.txt", "a") as file:
    file.write("This line was added using append mode.\n")

## Expected Result

The existing contents of context_output.txt are preserved.

A new line is added at the end:

This line was added using append mode.

## Important Point

Mode `"a"` means append.

It does NOT erase existing content.

## Checklist

- [ ] Created 08_with_open_append.py
- [ ] Created 08_with_open_append.md
- [ ] Ran the program
- [ ] Verified the new line