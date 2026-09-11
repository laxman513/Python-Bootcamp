# Program 12 — Modify an Existing Column

## Objective
Learn how to modify values in an existing Pandas column.

## Concepts
- Updating columns
- Vectorized operations
- Arithmetic on columns

## Example

df["Salary"] = df["Salary"] * 1.10

This increases every salary by 10%.

## Expected Output
All salaries should increase by 10%.

## Key Point
Pandas performs the operation on the complete column.

## Run
python 12_modify_column.py