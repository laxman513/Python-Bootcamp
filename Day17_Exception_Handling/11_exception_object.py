try:
    number = int("abc")

except ValueError as error:
    print("An error occurred")
    print("Error message:", error)

print("Program completed")