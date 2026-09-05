try:
    with open("missing.txt", "r") as file:
        content = file.read()

    print(content)

except FileNotFoundError:
    print("File not found.")

finally:
    print("Finally block executed.")