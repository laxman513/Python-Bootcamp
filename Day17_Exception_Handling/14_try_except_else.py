try:
    number = int(input("Please a Number:"))
    result = 1000 / number

except ValueError:
     print("Please enter a valid number")

except ZeroDivisionError:
     print("Number cannot be zero")

else:
    print("Division successful")
    print("Result:", result)

print("Program completed")