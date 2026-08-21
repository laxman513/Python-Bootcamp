print("Program started")

try:
    file = open("employee.txt", "r")
    print(file.read())
    file.close()

except FileNotFoundError:
    print("The file does not exist")

print("Program completed")