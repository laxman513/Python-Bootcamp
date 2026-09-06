# Program 20 — filter() and reduce()

## Objective
Learn how to filter values and reduce a collection to one value.

## Part 1 — filter()

filter() keeps elements for which the function returns True.

Example:

numbers = [1, 2, 3, 4, 5, 6]

result = filter(lambda x: x % 2 == 0, numbers)

Expected:

[2, 4, 6]

## Part 2 — reduce()

reduce() repeatedly combines elements and produces one final value.

Example:

[1, 2, 3, 4]

1 + 2 = 3
3 + 3 = 6
6 + 4 = 10

Expected:

10

## Important

reduce() must be imported from functools.

from functools import reduce