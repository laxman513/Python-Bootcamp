# Program 11 — Add a New Column

## Objective
Learn how to add a new column to a Pandas DataFrame.

## Concepts
- Adding a column
- Column assignment
- Calculating values from existing columns

## Example

df["Bonus"] = df["Salary"] * 0.10

This creates a new Bonus column.

## Expected Output
A new Bonus column should appear in the DataFrame.

## Key Point
Pandas allows us to create a new column using:

df["NewColumn"] = values

The number of values must match the number of rows.

## Run
python 11_add_column.py