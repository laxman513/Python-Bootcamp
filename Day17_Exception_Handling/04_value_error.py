print("Program started")

try:
    age = int("abc")
    print("Age:", age)

except ValueError:
    print("Invalid value. Please enter a number.")

print("Program completed")