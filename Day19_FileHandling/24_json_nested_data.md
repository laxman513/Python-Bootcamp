# Program 24 — Nested JSON Data

## Objective

Learn how to create, write, read, and access nested JSON data.

## Concepts

- Nested dictionaries
- Lists inside dictionaries
- Dictionaries inside dictionaries
- json.dump()
- json.load()

## Example Structure

{
    "name": "Rahul",
    "age": 20,
    "address": {
        "city": "Hyderabad",
        "state": "Telangana"
    },
    "subjects": [
        "Python",
        "Math",
        "Science"
    ]
}

## Important

Nested values are accessed step by step.

student["address"]["city"]

student["subjects"][0]

## Expected Output

Name: Rahul
City: Hyderabad
State: Telangana
First Subject: Python

## Checklist

- [ ] Created 24_json_nested_data.py
- [ ] Created 24_json_nested_data.md
- [ ] Used nested dictionary
- [ ] Used list inside dictionary
- [ ] Used json.dump()
- [ ] Used json.load()
- [ ] Accessed nested values