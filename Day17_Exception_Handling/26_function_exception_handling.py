def divide_numbers(a, b):
    try:
        result = a / b
        return result

    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None


print("Result:", divide_numbers(10, 2))
print("Result:", divide_numbers(10, 0))