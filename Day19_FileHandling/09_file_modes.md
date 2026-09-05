# Program 9 — Understanding File Modes

## Objective

Understand the basic file modes used with open().

## Important Modes

| Mode | Meaning |
|------|---------|
| r | Read |
| w | Write |
| a | Append |

## Behavior

### "r" — Read

Reads an existing file.

It gives an error if the file does not exist.

### "w" — Write

Creates a new file if it doesn't exist.

If the file already exists, its previous contents are replaced.

### "a" — Append

Creates a new file if it doesn't exist.

If the file already exists, new data is added at the end.

## Program

The program demonstrates all three modes.

## Checklist

- [ ] Created 09_file_modes.py
- [ ] Created 09_file_modes.md
- [ ] Understand r
- [ ] Understand w
- [ ] Understand a
- [ ] Ran the program