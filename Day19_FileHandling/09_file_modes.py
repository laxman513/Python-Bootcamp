# Read mode
with open("context_output.txt", "r") as file:
    content = file.read()

print("READ MODE:")
print(content)

# Append mode
with open("context_output.txt", "a") as file:
    file.write("Added using append mode.\n")

print("APPEND completed.")

# Read again
with open("context_output.txt", "r") as file:
    content = file.read()

print("\nFILE AFTER APPEND:")
print(content)