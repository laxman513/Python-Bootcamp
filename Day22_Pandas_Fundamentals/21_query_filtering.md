# Program 21 — query() for Filtering

## Objective
Learn how to filter DataFrame rows using Pandas query().

## Concepts
- query()
- Conditional filtering
- Comparing query() with boolean indexing

## Example

df.query("Salary > 70000")

This returns employees whose salary is greater than 70000.

## Why query()?

Instead of:

df[df["Salary"] > 70000]

we can write:

df.query("Salary > 70000")

## Run

python 21_query_filtering.py