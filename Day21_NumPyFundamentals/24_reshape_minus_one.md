# Program 24 — reshape() with -1

## Objective

Learn how NumPy automatically calculates one dimension when
`-1` is used in reshape().

## Concept

When one dimension is `-1`, NumPy calculates that dimension
automatically based on the total number of elements.

## Examples

6 elements:

reshape(2, -1) → (2, 3)

reshape(3, -1) → (3, 2)

reshape(-1, 1) → (6, 1)

## Run

python 24_reshape_minus_one.py