# Program 27 — Creating Directories

## Objective

Learn how to create directories using pathlib.

## Concepts

- Path.mkdir()
- exists()
- Directory creation
- parents
- exist_ok

## Important Method

mkdir()

creates a directory.

Example:

Path("data").mkdir()

## exist_ok=True

If the directory already exists, Python normally raises an error.

Using:

mkdir(exist_ok=True)

means:

"Create the directory if it doesn't exist. If it already exists, don't
raise an error."

## Why this matters

Applications frequently need to create folders for:

- datasets
- logs
- model files
- output files
- temporary files

## Expected Output

Data directory created or already exists.

## Checklist

- [ ] Created 27_pathlib_create_directory.py
- [ ] Created 27_pathlib_create_directory.md
- [ ] Used mkdir()
- [ ] Used exist_ok=True
- [ ] Ran the program
- [ ] Verified data folder