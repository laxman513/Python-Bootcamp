# Program 19 — map() Function

## Objective
Learn how to apply a function to every item in a collection.

## Concepts
- map()
- lambda with map()
- converting map result to list

## Syntax

map(function, iterable)

## Example

numbers = [1, 2, 3, 4, 5]

result = map(lambda x: x * 2, numbers)

## Expected Output

[2, 4, 6, 8, 10]

## Key Point

map() applies the given function to every element.