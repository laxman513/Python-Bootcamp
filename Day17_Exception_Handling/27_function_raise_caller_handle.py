def divide_numbers(a, b):

    if b == 0:
        raise ZeroDivisionError("Denominator cannot be zero")

    return a / b


try:
    result = divide_numbers(10, 0)
    print("Result:", result)

except ZeroDivisionError as error:
    print("Error:", error)

print("Program completed")