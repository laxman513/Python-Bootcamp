# Program 22 — Conditional Column

## Objective
Create a new column based on a condition.

## Concepts
- np.where()
- Conditional columns
- Feature creation

## Example

np.where(df["Salary"] >= 70000, "High", "Normal")

If salary >= 70000:
    High

Otherwise:
    Normal

## ML Connection

Creating new columns from existing data is called feature engineering.

## Run

python 22_conditional_column.py