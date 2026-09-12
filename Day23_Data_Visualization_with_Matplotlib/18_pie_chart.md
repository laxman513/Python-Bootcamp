# Program 18 — Pie Chart

## Objective

Learn how to create a pie chart using Matplotlib.

## Concepts

- Pie chart
- `plt.pie()`
- Percentages
- Labels
- `autopct`
- `startangle`

## Explanation

A pie chart shows how a total is divided among categories.

Example:

IT       → 40 employees
HR       → 20 employees
Finance  → 15 employees
Sales    → 25 employees

The pie chart shows each department's percentage of total employees.

## Important Function

```python
plt.pie(values, labels=labels)