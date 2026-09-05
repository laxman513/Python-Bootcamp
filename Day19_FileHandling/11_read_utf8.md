# Program 11 — Reading a UTF-8 File

## Objective

Learn how to read a UTF-8 encoded text file correctly.

## Concepts

- UTF-8 encoding
- Reading text files
- `encoding="utf-8"`
- `with open()`

## Steps

1. Use the file created in Program 10.
2. Open it in read mode.
3. Specify UTF-8 encoding.
4. Read and display the contents.

## Code

with open("encoding_test.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)

## Expected Output

Python File Handling
Hello World
నమస్కారం
తెలుగు భాష

## Important Point

The encoding used for reading should normally match the encoding used when
the file was created.

## Checklist

- [ ] Created 11_read_utf8.py
- [ ] Created 11_read_utf8.md
- [ ] Used encoding="utf-8"
- [ ] Ran the program
- [ ] Verified Telugu text