# Program 20 — Fill Missing Values

## Objective
Learn how to replace missing values.

## Concepts
- fillna()
- Filling with a constant
- Filling numerical values
- Mean imputation

## Example

df["Age"] = df["Age"].fillna(df["Age"].mean())

This replaces missing Age values with the average age.

## Why?

Machine Learning algorithms generally require numerical inputs without missing values.

Therefore, missing values often need to be handled before model training.

## Run

python 20_fill_missing_values.py