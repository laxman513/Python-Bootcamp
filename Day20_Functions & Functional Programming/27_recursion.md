# Program 27 — Recursion

## Objective

Understand how a function can call itself.

## Example

def countdown(number):

    if number == 0:
        return

    print(number)

    countdown(number - 1)

## Expected Output

3
2
1

## Key Concepts

- Recursive function
- Base condition
- Recursive call

## Important

Every recursive function needs a base condition.

Without a base condition, the function will keep calling itself.