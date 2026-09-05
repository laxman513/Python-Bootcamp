# Program 10 — File Encoding

## Objective

Learn how to specify file encoding when reading and writing text files.

## Concept

Encoding determines how text characters are stored and interpreted.

A commonly used encoding is:

UTF-8

## Why UTF-8?

UTF-8 supports:

- English
- Telugu
- Hindi
- many other languages
- symbols and special characters

## Program

The program creates a UTF-8 text file containing English and Telugu text.

## Important Syntax

with open("file.txt", "w", encoding="utf-8") as file:

## Checklist

- [ ] Created 10_file_encoding.py
- [ ] Created 10_file_encoding.md
- [ ] Used encoding="utf-8"
- [ ] Ran the program
- [ ] Verified the file contents