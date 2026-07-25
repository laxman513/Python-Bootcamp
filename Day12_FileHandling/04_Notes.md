# ==========================================================
# Day 12 - File Handling Notes
# ==========================================================

## What is a File?

A file is a collection of data stored permanently in secondary storage.

Examples:
- Text File (.txt)
- CSV File (.csv)
- JSON File (.json)
- PDF File (.pdf)

---

## Why do we use files?

- Permanent Storage
- Store Logs
- Store Reports
- Store Student Records
- Store Configuration
- Data Sharing

---

## open()

Syntax

```python
file = open("student.txt", "r")
```

---

## File Modes

| Mode | Description |
|------|-------------|
| r | Read |
| w | Write (Deletes old data) |
| a | Append |
| x | Create New File |
| r+ | Read + Write |
| w+ | Write + Read |
| a+ | Append + Read |

---

## File Methods

read()

Reads entire file.

readline()

Reads one line.

readlines()

Returns list of lines.

write()

Writes data.

close()

Closes file.

---

## with Statement

```python
with open("student.txt","r") as file:
    print(file.read())
```

Advantages

- Automatically closes file
- Cleaner code
- Exception safe

---

## String Methods Used

upper()

lower()

strip()

split()

splitlines()

replace()

count()

isdigit()

isalpha()

isalnum()

isspace()

isupper()

islower()

---

## Common File Operations

Read File

Write File

Append File

Copy File

Merge Files

Search Word

Replace Word

Count Lines

Count Words

Count Characters

Backup File

Compare Files

Reverse File

Word Frequency

---

## Best Practices

✅ Always use with

✅ Close resources properly

✅ Handle exceptions

✅ Use meaningful file names

✅ Keep backup before modifying files

---

## Interview Tips

Difference between read(), readline(), readlines()

Difference between w and a

Difference between split() and splitlines()

Why use with?

How to copy a file?

How to count words?

How to count lines?

How to search text?

How to replace text?

How to merge files?

---

## Summary

Day 12 covered:

✔ File Handling Basics

✔ Reading Files

✔ Writing Files

✔ Appending Files

✔ File Processing

✔ Text Processing

✔ Reports

✔ Mini Project