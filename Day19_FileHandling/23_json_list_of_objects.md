# Program 23 — JSON List of Objects

## Objective

Learn how to store and read multiple records using JSON.

## Concepts

- JSON list
- JSON objects
- Python list
- Python dictionaries
- json.dump()
- json.load()
- Iterating through JSON data

## Structure

[
    {
        "name": "Rahul",
        "age": 20,
        "marks": 85
    },
    {
        "name": "Priya",
        "age": 21,
        "marks": 92
    }
]

The outer structure is a list.

Each item inside the list is a dictionary/object.

## Expected Output

Rahul - 20 - 85
Priya - 21 - 92
Arjun - 19 - 78

## Why This Matters

This structure is very common in:

- REST APIs
- configuration files
- datasets
- web applications
- AI/ML applications

## Checklist

- [ ] Created 23_json_list_of_objects.py
- [ ] Created 23_json_list_of_objects.md
- [ ] Created students.json
- [ ] Used json.dump()
- [ ] Used json.load()
- [ ] Iterated through records