# Program 07 — Selecting Multiple Columns

## Objective

Learn how to select multiple columns from a DataFrame.

## Syntax

df[["Column1", "Column2"]]

## Important

Single column:

df["Salary"]

Returns a Series.

Multiple columns:

df[["Age", "Salary"]]

Returns a DataFrame.

## Key Point

Single brackets → Series

Double brackets → DataFrame