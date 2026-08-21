class AgeError(Exception):
    pass


age = 15

try:
    if age < 18:
        raise AgeError("Age must be 18 or above")

except AgeError as error:
    print("Age Error:", error)

print("Program completed")