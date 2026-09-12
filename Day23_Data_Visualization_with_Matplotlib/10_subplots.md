# Program 10 — Subplots

## Objective

Learn how to display multiple plots inside one figure.

## Concept

plt.subplot(rows, columns, position)

## Example

plt.subplot(2, 1, 1)

means:

2 rows
1 column
1st plot

Then:

plt.subplot(2, 1, 2)

means:

2 rows
1 column
2nd plot

## Layout

The result is:

+----------------------+
|    Monthly Sales     |
+----------------------+
|   Monthly Expenses   |
+----------------------+

## tight_layout()

plt.tight_layout()

automatically adjusts spacing between plots.

## figsize()

plt.figure(figsize=(10, 6))

controls the size of the overall figure.

## Run

python 10_subplots.py