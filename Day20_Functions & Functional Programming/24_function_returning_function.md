# Program 24 — Function Returning Another Function

## Objective

Learn how a function can return another function.

## Example

def create_multiplier(number):

    def multiplier(value):
        return value * number

    return multiplier

double = create_multiplier(2)

result = double(10)

## Expected Output

20

## Key Point

A function can return another function as its result.

This concept is the foundation for closures and decorators.