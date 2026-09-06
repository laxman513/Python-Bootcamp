# Program 22 — List Comprehension with Condition

## Objective

Learn how to filter elements while creating a new list.

## Example

numbers = [1, 2, 3, 4, 5, 6]

even_numbers = [
    number
    for number in numbers
    if number % 2 == 0
]

## Expected Output

[2, 4, 6]

## General Syntax

[expression for item in iterable if condition]

## Key Point

The if condition decides which elements are included.