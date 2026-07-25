"""
==========================================================
Day 12 - File Handling
02_Assignments_With_Solutions.py
==========================================================
"""

# ==========================================================
# Assignment 1
# Write "Hello Python" into hello.txt
# ==========================================================

print("\nAssignment 1")
print("-" * 40)

# ---------- Solution ----------

with open("hello.txt", "w") as file:

    file.write("Hello Python")

print("Data Written Successfully")


# ==========================================================
# Assignment 2
# Read and display hello.txt
# ==========================================================

print("\nAssignment 2")
print("-" * 40)

# ---------- Solution ----------

with open("hello.txt", "r") as file:

    print(file.read())


# ==========================================================
# Assignment 3
# Append your name to hello.txt
# ==========================================================

print("\nAssignment 3")
print("-" * 40)

# ---------- Solution ----------

with open("hello.txt", "a") as file:

    file.write("\nLaxman")

print("Name Added")


# ==========================================================
# Assignment 4
# Count number of characters
# ==========================================================

print("\nAssignment 4")
print("-" * 40)

# ---------- Solution ----------

with open("hello.txt", "r") as file:

    data = file.read()

print("Characters :", len(data))


# ==========================================================
# Assignment 5
# Count number of words
# ==========================================================

print("\nAssignment 5")
print("-" * 40)

# ---------- Solution ----------

with open("hello.txt", "r") as file:

    data = file.read()

print("Words :", len(data.split()))


# ==========================================================
# Assignment 6
# Count number of lines
# ==========================================================

print("\nAssignment 6")
print("-" * 40)

# ---------- Solution ----------

with open("hello.txt", "r") as file:

    print("Lines :", len(file.readlines()))


# ==========================================================
# Assignment 7
# Convert file content to uppercase
# ==========================================================

print("\nAssignment 7")
print("-" * 40)

# ---------- Solution ----------

with open("hello.txt", "r") as file:

    data = file.read()

print(data.upper())


# ==========================================================
# Assignment 8
# Search a word
# ==========================================================

print("\nAssignment 8")
print("-" * 40)

# ---------- Solution ----------

word = input("Enter Word : ")

with open("hello.txt", "r") as file:

    data = file.read()

if word in data:

    print("Found")

else:

    print("Not Found")


# ==========================================================
# Assignment 9
# Copy hello.txt to backup.txt
# ==========================================================

print("\nAssignment 9")
print("-" * 40)

# ---------- Solution ----------

with open("hello.txt", "r") as source:

    data = source.read()

with open("backup.txt", "w") as destination:

    destination.write(data)

print("Backup Created")


# ==========================================================
# Assignment 10
# Print every line separately
# ==========================================================

print("\nAssignment 10")
print("-" * 40)

# ---------- Solution ----------

with open("hello.txt", "r") as file:

    for line in file:

        print(line.strip())