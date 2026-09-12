# Program 22 — Department Salary Visualization

## Objective

Calculate average salary by department and visualize the result.

## Concepts

- Pandas groupby
- Mean
- Matplotlib bar chart
- Aggregated data
- Business analysis

## Tasks

1. Load employee data.
2. Fill missing salaries.
3. Group employees by Department.
4. Calculate average salary.
5. Create a bar chart.

## Important Code

```python
df.groupby("Department")["Salary"].mean()