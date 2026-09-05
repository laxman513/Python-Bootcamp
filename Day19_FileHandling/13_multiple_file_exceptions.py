try:
    with open("missing.txt", "r") as file:
        content = file.read()

    print(content)

except FileNotFoundError:
    print("File not found: missing.txt")

except PermissionError:
    print("Permission denied: cannot access the file.")