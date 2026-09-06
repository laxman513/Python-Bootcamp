# Program 26 — Closures

## Objective

Understand how an inner function remembers variables from its enclosing function.

## Example

def create_multiplier(number):

    def multiplier(value):
        return value * number

    return multiplier

double = create_multiplier(2)

print(double(10))

## Expected Output

20

## Key Point

A closure occurs when an inner function remembers and uses variables
from its enclosing function even after the outer function has finished.

## Important

number = 2 belongs to create_multiplier().

value = 10 belongs to multiplier().

double remembers number = 2.