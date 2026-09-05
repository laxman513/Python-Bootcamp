# Program 12 — Handling FileNotFoundError

## Objective

Learn how to safely handle the situation where a file does not exist.

## Problem

If we try:

open("missing.txt", "r")

and the file doesn't exist, Python raises:

FileNotFoundError

Without exception handling, the program stops with an error.

## Solution

Use try-except.

## Structure

try:
    # Code that may cause an error
except FileNotFoundError:
    # Handle missing file

## Expected Output

The program should display a friendly message instead of crashing.

## Checklist

- [ ] Created 12_file_not_found.py
- [ ] Created 12_file_not_found.md
- [ ] Used try
- [ ] Used except FileNotFoundError
- [ ] Ran the program
- [ ] Verified the program doesn't crash