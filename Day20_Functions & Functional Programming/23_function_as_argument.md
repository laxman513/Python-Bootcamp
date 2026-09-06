# Program 23 — Function as an Argument

## Objective

Learn that functions can be passed as arguments to other functions.

## Example

def calculate(operation, a, b):
    return operation(a, b)

def add(a, b):
    return a + b

result = calculate(add, 10, 20)

## Expected Output

30

## Key Point

In Python, functions are first-class objects.

This means a function can be:

- stored in a variable
- passed as an argument
- returned from another function