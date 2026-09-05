# Program 25 — pathlib Basics

## Objective

Learn how to use pathlib to work with file and folder paths.

## Concepts

- pathlib
- Path
- Current directory
- File paths
- Path objects

## Why pathlib?

pathlib provides an object-oriented way to work with files and directories.

Instead of manually constructing paths like:

"D:\\Development\\Python\\file.txt"

we can use:

Path("file.txt")

## Important Methods

Path.cwd()
→ Current working directory

Path("file.txt")
→ Represents a file path

exists()
→ Checks whether a path exists

## Expected Output

The program displays:

- Current working directory
- Whether output.txt exists
- The path of output.txt

## Checklist

- [ ] Created 25_pathlib_basics.py
- [ ] Created 25_pathlib_basics.md
- [ ] Imported Path
- [ ] Used Path.cwd()
- [ ] Used exists()
- [ ] Ran the program