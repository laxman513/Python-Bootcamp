from functools import reduce

numbers = [1, 2, 3, 4, 5, 6]

# filter()
even_numbers = filter(lambda a: a % 2 == 0, numbers)

print("Even Numbers:", list(even_numbers))

# reduce()
numbers = [1, 2, 3, 4]

total = reduce(lambda a, b: a + b, numbers)

print("Total:", total)