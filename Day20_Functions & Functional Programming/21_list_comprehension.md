# Program 21 — List Comprehension

## Objective

Learn how to create a new list using a compact Python syntax.

## Normal approach

numbers = [1, 2, 3, 4, 5]

squares = []

for number in numbers:
    squares.append(number * number)

## List comprehension

squares = [number * number for number in numbers]

## Expected Output

[1, 4, 9, 16, 25]

## Key Point

List comprehension is a concise way to create a list from an iterable.

## General Syntax

[expression for item in iterable]

## Checklist

- [ ] Understand list comprehension
- [ ] Convert a normal for loop to comprehension
- [ ] Understand expression, item and iterable