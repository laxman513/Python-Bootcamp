# Program 24 — GroupBy with Multiple Aggregations

## Objective
Perform multiple calculations on grouped data.

## Concepts
- groupby()
- agg()
- mean()
- min()
- max()
- count()

## Example

df.groupby("Department")["Salary"].agg(
    ["count", "mean", "min", "max"]
)

## Expected Output

For every department, display:

- Employee count
- Average salary
- Minimum salary
- Maximum salary

## Run

python 24_groupby_agg.py