# Program 1 — Reading a Text File

## Objective

Learn how to:

1. Create a text file.
2. Open a text file.
3. Read the contents of a text file.
4. Close the file.

---

## Step 1 — Create a sample text file

Inside the Day19_FileHandling folder, create:

sample.txt

Add:

Hello, welcome to Python File Handling.
This is my first text file program.

---

## Step 2 — Open the file

Python provides the `open()` function.

Syntax:

open("filename", "mode")

Example:

file = open("sample.txt", "r")

"r" means read mode.

---

## Step 3 — Read the contents

Use:

content = file.read()

This reads the complete contents of the file.

---

## Step 4 — Display the contents

Use:

print(content)

---

## Step 5 — Close the file

Use:

file.close()

Closing the file releases the file resource.

---

## Program

Create:

01_read_text_file.py

Code:

file = open("sample.txt", "r")

content = file.read()

print(content)

file.close()

---

## Expected Output

Hello, welcome to Python File Handling.
This is my first text file program.

---

## Important Concepts

open()
    ↓
Open a file

read()
    ↓
Read file contents

close()
    ↓
Close the file

---

## Important Note

In later programs we will learn the recommended way of opening files using:

with open(...)

For this first program, we intentionally use open() and close() separately so that the basic file-handling process is clear.

---

## Program 1 Checklist

[ ] Create Day19_FileHandling folder

[ ] Create sample.txt

[ ] Add text to sample.txt

[ ] Create 01_read_text_file.py

[ ] Use open()

[ ] Use read()

[ ] Use print()

[ ] Use close()

[ ] Run the program

[ ] Verify the output