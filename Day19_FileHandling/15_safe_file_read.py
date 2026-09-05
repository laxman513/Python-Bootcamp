def read_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()

    except FileNotFoundError:
        return f"Error: '{filename}' was not found."


# Test with an existing file
content = read_file("context_output.txt")
print(content)

print("-" * 40)

# Test with a missing file
content = read_file("does_not_exist.txt")
print(content)