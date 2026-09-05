# Program 3 — Appending to a Text File

## Objective

Learn how to:

1. Open an existing file in append mode.
2. Add new content without deleting existing content.
3. Understand the difference between write mode and append mode.
4. Use the `write()` method with append mode.

---

## File Mode

Python provides append mode:

open("filename", "a")

The `"a"` means:

append mode

---

## Important Behavior of "a"

If the file does not exist:

Python creates the file.

If the file already exists:

Python keeps the existing contents and adds new content at the end.

Therefore:

"a" = append

---

## Difference Between "w" and "a"

Write mode:

open("file.txt", "w")

Existing content is overwritten.

Append mode:

open("file.txt", "a")

Existing content is preserved and new content is added at the end.

---

## Program

Create:

03_append_text_file.py

The program should:

1. Open `output.txt` in append mode.
2. Add two new lines.
3. Close the file.

---

## Existing File

The `output.txt` file created in Program 2 should contain:

Python File Handling
Writing data to a text file.

---

## After Running Program 3

The file should contain:

Python File Handling
Writing data to a text file.
This line was added using append mode.
The original content was preserved.

---

## Important Concepts

open()
    ↓
Open/create file

"a"
    ↓
Append mode

write()
    ↓
Add data at the end

close()
    ↓
Close file

---

## Important Note

Append mode does NOT erase existing content.

Every time the program runs, the new content is added again.

For example, if you run the program twice, the appended lines will appear twice.

---

## Program 3 Checklist

[ ] Create 03_append_text_file.md

[ ] Create 03_append_text_file.py

[ ] Verify output.txt exists

[ ] Use open()

[ ] Use "a" mode

[ ] Use write()

[ ] Use close()

[ ] Run the program

[ ] Open output.txt

[ ] Verify original content is preserved

[ ] Verify new content is added at the end

[ ] Run the program a second time

[ ] Observe that the new lines are added again