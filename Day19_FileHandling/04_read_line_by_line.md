# Program 4 — Reading a File Line by Line

## Objective

Learn how to read a text file one line at a time.

We will learn:

1. `read()`
2. `readline()`
3. Difference between reading the entire file and reading one line.
4. How to read multiple lines using `readline()`.

---

## `read()`

The `read()` method reads the complete contents of a file.

Example:

content = file.read()

---

## `readline()`

The `readline()` method reads one line at a time.

Example:

line = file.readline()

Calling `readline()` again reads the next line.

---

## Important Concept

If a file contains:

Line 1
Line 2
Line 3

Then:

file.readline()

returns:

Line 1

Calling it again returns:

Line 2

Calling it again returns:

Line 3

---

## Program

Create:

04_read_line_by_line.py

The program will:

1. Open `output.txt` in read mode.
2. Read the first line.
3. Read the second line.
4. Read the third line.
5. Display each line.
6. Close the file.

---

## Expected Output

The exact output depends on the current contents of `output.txt`.

For example:

Python File Handling
Writing data to a text file.
This line was added using append mode.

---

## Important Concepts

read()
    ↓
Reads the complete file

readline()
    ↓
Reads one line

Each call to readline()
moves to the next line.

---

## Program 4 Checklist

[ ] Create 04_read_line_by_line.md

[ ] Create 04_read_line_by_line.py

[ ] Open output.txt in read mode

[ ] Use readline()

[ ] Read multiple lines

[ ] Print the lines

[ ] Close the file

[ ] Run the program

[ ] Verify the output