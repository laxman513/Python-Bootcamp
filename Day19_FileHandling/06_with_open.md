# Program 6 — Using with open()

## Objective

Learn how to use Python's context manager for file handling.

We will learn:

1. The `with` statement.
2. `with open()`.
3. Automatic file closing.
4. Why `with open()` is preferred over manually calling `close()`.

---

## Previous Approach

In earlier programs we used:

file = open("output.txt", "r")

content = file.read()

print(content)

file.close()

The programmer must remember to close the file.

---

## Recommended Approach

Python provides a better way:

with open("output.txt", "r") as file:
    content = file.read()
    print(content)

The file is automatically closed when the `with` block finishes.

---

## What is a Context Manager?

A context manager manages a resource automatically.

For files:

with open(...) as file:

means:

1. Open the file.
2. Execute the code inside the `with` block.
3. Automatically close the file when the block finishes.

---

## Important Syntax

with open("filename", "mode") as file:
    # work with the file

The code inside the `with` block must be indented.

---

## Program

Create:

06_with_open.py

The program will:

1. Open output.txt using `with open()`.
2. Read the contents.
3. Display the contents.
4. Allow Python to automatically close the file.

---

## Expected Output

The contents of output.txt should be displayed.

Example:

Python File Handling
Writing data to a text file.
This line was added using append mode.
The original content was preserved.

---

## Why is with open() better?

Manual approach:

file = open(...)
...
file.close()

Problem:

If an exception occurs before `file.close()`, the file may not be closed properly.

Context manager:

with open(...) as file:
    ...

Python automatically handles closing the file.

---

## Important Rule

For normal Python file handling, prefer:

with open(...) as file:

instead of:

file = open(...)
...
file.close()

---

## Program 6 Checklist

[ ] Create 06_with_open.md

[ ] Create 06_with_open.py

[ ] Use with open()

[ ] Use read()

[ ] Print file contents

[ ] Do not use file.close()

[ ] Run the program

[ ] Verify the output

[ ] Understand automatic file closing