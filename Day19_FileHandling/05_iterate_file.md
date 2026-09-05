# Program 5 — Iterating Through a File

## Objective

Learn how to:

1. Iterate through a text file using a `for` loop.
2. Read one line at a time.
3. Process each line.
4. Understand why file iteration is useful for large files.

---

## Basic Syntax

A file object can be directly used with a `for` loop.

Example:

file = open("output.txt", "r")

for line in file:
    print(line, end="")

file.close()

---

## How It Works

Python automatically reads the file one line at a time.

For example:

output.txt

Line 1
Line 2
Line 3

The loop processes:

Iteration 1 → Line 1
Iteration 2 → Line 2
Iteration 3 → Line 3

---

## Why Use a for Loop?

Instead of:

line1 = file.readline()
line2 = file.readline()
line3 = file.readline()

we can use:

for line in file:
    print(line, end="")

This automatically continues until the end of the file.

---

## Memory Advantage

When iterating through a file this way, Python processes the file progressively rather than requiring the entire file to be loaded into memory at once.

This becomes useful when working with large files.

---

## Program

Create:

05_iterate_file.py

The program will:

1. Open output.txt.
2. Iterate through every line.
3. Display each line.
4. Close the file.

---

## Expected Output

The output should contain every line currently present in output.txt.

Example:

Python File Handling
Writing data to a text file.
This line was added using append mode.
The original content was preserved.

---

## Important Concepts

File object
    ↓
for loop
    ↓
One line at a time
    ↓
Process the line

---

## Program 5 Checklist

[ ] Create 05_iterate_file.md

[ ] Create 05_iterate_file.py

[ ] Open output.txt

[ ] Use a for loop

[ ] Process each line

[ ] Print each line

[ ] Close the file

[ ] Run the program

[ ] Verify all lines are displayed