# Program 19 — CSV DictReader

## Objective

Learn how to read CSV rows as dictionaries.

## Concepts

- csv.DictReader
- Dictionary
- Column names
- Accessing values using keys

## CSV

Name,Age,Marks
Rahul,20,85
Priya,21,92
Arjun,19,78

## Normal csv.reader()

A row looks like:

["Rahul", "20", "85"]

## csv.DictReader()

A row looks like:

{
    "Name": "Rahul",
    "Age": "20",
    "Marks": "85"
}

## Advantage

We can access values using column names:

row["Name"]
row["Age"]
row["Marks"]

This is easier to understand and maintain.

## Expected Output

Name: Rahul, Age: 20, Marks: 85
Name: Priya, Age: 21, Marks: 92
Name: Arjun, Age: 19, Marks: 78

## Checklist

- [ ] Created 19_csv_dict_reader.py
- [ ] Created 19_csv_dict_reader.md
- [ ] Used csv.DictReader
- [ ] Accessed columns by name
- [ ] Ran the program