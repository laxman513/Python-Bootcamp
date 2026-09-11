# Program 04 — DataFrame from Dictionary

## Objective

Create a Pandas DataFrame using a Python dictionary.

## Concept

Dictionary keys become column names.

Dictionary values become column data.

Example:

data = {
    "Name": ["Rahul", "Priya"],
    "Age": [25, 30]
}

df = pd.DataFrame(data)

## Why This Is Important

Real-world data often comes from:

- JSON
- APIs
- databases
- CSV files

Pandas can easily convert structured data into a DataFrame.