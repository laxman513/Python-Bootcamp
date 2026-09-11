# Program 23 — groupby()

## Objective
Learn how to group rows based on a column.

## Concepts
- groupby()
- Aggregation
- mean()
- sum()
- Multiple groups

## Example

df.groupby("Department")["Salary"].mean()

This calculates the average salary for each department.

## Why is groupby() important?

It is used extensively in:

- Data analysis
- Reporting
- Business analytics
- Feature engineering
- Exploratory Data Analysis (EDA)

## Run

python 23_groupby.py