# Program 14 — Sort DataFrame

## Objective
Learn how to sort a DataFrame based on a column.

## Concepts
- sort_values()
- ascending=True
- ascending=False

## Example

df.sort_values("Salary")

Sorts salary from lowest to highest.

df.sort_values("Salary", ascending=False)

Sorts salary from highest to lowest.

## Expected Output
Employees should be ordered according to salary.

## Run
python 14_sort_dataframe.py