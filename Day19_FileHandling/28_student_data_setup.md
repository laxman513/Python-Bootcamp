# Program 28 — Student Data File Setup

## Objective

Create the basic structure for a Student Data File Manager using pathlib and JSON.

## Concepts

- pathlib.Path
- mkdir()
- exists()
- JSON
- json.dump()
- with open()
- UTF-8 encoding

## Requirements

Create a `data` directory.

Inside the directory, create:

students.json

The initial JSON file should contain an empty list:

[]

## Expected Structure

Day19_FileHandling/
│
├── data/
│   └── students.json
│
└── 28_student_data_setup.py

## Expected Output

Data directory created or already exists.
Student data file created successfully.
File exists: True

## Run

python 28_student_data_setup.py