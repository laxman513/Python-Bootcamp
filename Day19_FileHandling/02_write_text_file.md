# Program 2 — Writing to a Text File

## Objective

Learn how to:

1. Open a file in write mode.
2. Write text into a file.
3. Understand write mode (`"w"`).
4. Understand what happens when a file already exists.

---

## File Mode

Python's `open()` function accepts a mode.

For writing:

open("filename", "w")

The `"w"` means:

write mode

---

## Important Behavior of "w"

If the file does not exist:

Python creates the file.

If the file already exists:

Python removes the existing contents and writes the new contents.

Therefore:

"w" = write / overwrite

---

## Program

Create:

02_write_text_file.py

The program should:

1. Open `output.txt` in write mode.
2. Write two lines.
3. Close the file.

---

## Expected File

After running the program, Python should create:

output.txt

Its contents should be:

Python File Handling
Writing data to a text file.

---

## Expected Output

The Python program does not need to print anything.

The result is the creation of:

output.txt

---

## Important Concepts

open()
    ↓
Open/create file

"w"
    ↓
Write mode

write()
    ↓
Write data

close()
    ↓
Close file

---

## Important Warning

Write mode can overwrite an existing file.

For example, if output.txt contains:

Old information

and we execute:

open("output.txt", "w")

the old contents will be removed.

---

## Program 2 Checklist

[ ] Create 02_write_text_file.md

[ ] Create 02_write_text_file.py

[ ] Use open()

[ ] Use "w" mode

[ ] Use write()

[ ] Use close()

[ ] Run the program

[ ] Verify output.txt is created

[ ] Open output.txt

[ ] Verify the contents

[ ] Understand that "w" overwrites existing content