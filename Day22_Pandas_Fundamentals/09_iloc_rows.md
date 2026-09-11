# Program 09 — Selecting Rows with iloc

## Objective

Learn how to select rows using integer positions.

## Syntax

df.iloc[position]

## Examples

df.iloc[0]

First row.

df.iloc[1:3]

Rows at positions 1 and 2.

## Important Difference

loc → label based

iloc → position based

Python slicing rules apply to iloc.
Therefore the ending position is excluded.