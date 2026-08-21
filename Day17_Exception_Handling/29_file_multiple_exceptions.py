filename = "employee.txt"

try:

    with open(filename, "r") as file:

        for line in file:
            print(line.strip())

except FileNotFoundError:
    print("File does not exist:", filename)

except PermissionError:
    print("Permission denied:", filename)

except Exception as error:
    print("Unexpected error:", error)

print("Program completed")