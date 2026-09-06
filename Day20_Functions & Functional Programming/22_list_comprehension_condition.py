# List comprehension with condition

numbers = [1, 2, 3, 4, 5, 6]

print("Numbers:", numbers)

even_numbers = [number for number in numbers if number % 2 == 0]

print("Even Numbers:", even_numbers)

even_numbers_using_filter = list(filter(lambda x: x % 2 == 0, numbers))

print("even", even_numbers_using_filter)