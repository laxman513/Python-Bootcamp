try:
    with open("employee.txt", "r") as file:
        data = file.read()

        print("File contents:")
        print(data)

except FileNotFoundError:
    print("Employee file was not found")

except PermissionError:
    print("You don't have permission to read this file")

print("Program completed")