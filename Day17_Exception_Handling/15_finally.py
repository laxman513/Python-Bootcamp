try:
    number = 10
    result = number / 0

    print("Result:", result)

except ZeroDivisionError:
    print("Cannot divide by zero")

finally:
    print("This block always executes")

print("Program completed")