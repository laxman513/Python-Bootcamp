print("Program started")

try:
    number = 10
    result = number / 0
    print("Result:", result)

except ZeroDivisionError:
    print("You cannot divide a number by zero")

print("Program completed")