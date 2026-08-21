def check_age(age):
    if age < 18:
        raise ValueError("Age must be 18 or above")

    print("Age is valid")


try:
    check_age(15)

except ValueError as error:
    print("Validation error:", error)

print("Program completed")