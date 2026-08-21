try:
    age = int(input("Enter your age: "))

    if age < 0:
        raise ValueError("Age cannot be negative")

    if age > 120:
        raise ValueError("Age cannot be greater than 120")

    print("Valid age:", age)

except ValueError as error:
    print("Invalid input:", error)

print("Program completed")