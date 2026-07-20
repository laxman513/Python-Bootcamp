raise ValueError("Invalid Input")

try:
    number = int(input("Enter number : "))
    result = 100 / number
    print(result)

except Exception as e:
    print("Error:", e)

except ValueError:
    print("Please enter valid number")

except ZeroDivisionError:
    print("Number can not be zero")

age = -5

if  age < 0:
    raise ValueError("Age should not negative")
