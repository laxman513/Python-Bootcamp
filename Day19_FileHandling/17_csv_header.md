# Program 17 — Reading CSV with a Header

## Objective

Learn how to read the header separately from the data rows.

## Concepts

- csv.reader()
- Header row
- next()
- Iterating over CSV rows

## CSV Structure

Name,Age,Marks
Rahul,20,85
Priya,21,92
Arjun,19,78

The first row is the header.

The remaining rows contain data.

## Important Concept

next(reader)

moves the CSV reader to the next row.

We use it to read the header separately.

## Expected Output

Header:
Name | Age | Marks

Student Data:
Rahul | 20 | 85
Priya | 21 | 92
Arjun | 19 | 78

## Checklist

- [ ] Created 17_csv_header.py
- [ ] Created 17_csv_header.md
- [ ] Used csv.reader()
- [ ] Used next()
- [ ] Separated header from data