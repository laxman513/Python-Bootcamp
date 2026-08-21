print("Program started")

try:
    result = 10 + "20"
    print(result)

except TypeError:
    print("Cannot add an integer and a string")

print("Program completed")