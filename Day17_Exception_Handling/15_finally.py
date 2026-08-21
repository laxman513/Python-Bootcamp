try:
    number = 10
    result = number / 0

    print("Result:", result)

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("Division successful")

finally:
    print("This block always executes")

# else:
#     print("Division ")

print("Program completed")