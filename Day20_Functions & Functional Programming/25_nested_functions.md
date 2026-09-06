# Program 25 — Nested Functions

## Objective

Learn how to define a function inside another function.

## Concepts

- Outer function
- Inner function
- Calling the inner function
- Scope of nested functions

## Example

def outer():
    def inner():
        print("Inside inner function")

    inner()

outer()

## Expected Output

Inside inner function

## Key Point

A function defined inside another function is called a nested function.

The inner function normally exists only within the scope of the outer function.