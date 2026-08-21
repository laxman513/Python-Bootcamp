file = None

try:
    file = open("employee.txt", "r")

    data = file.read()

    print(data)

except FileNotFoundError:
    print("File not found")

finally:
    if file is not None:
        file.close()
        print("File closed")

print("Program completed")