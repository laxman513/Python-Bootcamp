try:
    number = int(input("Enter a number: "))

    result = 100 / number

    print("Result:", result)

except (ValueError, ZeroDivisionError):
    print("Invalid input or division by zero")

print("Program completed")