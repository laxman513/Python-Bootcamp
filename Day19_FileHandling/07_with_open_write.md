# Program 7 — Using with open() for Writing

## Objective

Learn how to use the `with open()` context manager while writing data to a file.

## Concepts

- `with open()`
- Write mode `"w"`
- Automatic file closing
- Writing multiple lines
- Difference between manual `close()` and context manager

## Steps

1. Open `context_output.txt` using `with open()`.
2. Use write mode `"w"`.
3. Write two lines.
4. The file automatically closes after the `with` block.

## Program

The program writes:

Python File Handling
Using with open() for writing.

## Expected Output

The program itself does not print anything.

A new file called `context_output.txt` should be created.

Its contents should be:

Python File Handling
Using with open() for writing.

## Important Point

Instead of:

file = open("file.txt", "w")
file.write("Hello")
file.close()

we can use:

with open("file.txt", "w") as file:
    file.write("Hello")

The `with` statement automatically closes the file.

## Checklist

- [ ] Created `07_with_open_write.py`
- [ ] Created `07_with_open_write.md`
- [ ] Ran the program
- [ ] Verified `context_output.txt`
- [ ] Verified the file contents