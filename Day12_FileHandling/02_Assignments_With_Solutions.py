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

# ==========================================================
# Assignment 11
# Count Number of Vowels
# ==========================================================

print("\nAssignment 11")
print("-" * 40)

# ---------- Solution ----------

with open("hello.txt", "r") as file:

    data = file.read().lower()

count = 0

for ch in data:

    if ch in "aeiou":

        count += 1

print("Vowels :", count)


# ==========================================================
# Assignment 12
# Count Number of Digits
# ==========================================================

print("\nAssignment 12")
print("-" * 40)

# ---------- Solution ----------

with open("hello.txt", "r") as file:

    data = file.read()

count = 0

for ch in data:

    if ch.isdigit():

        count += 1

print("Digits :", count)


# ==========================================================
# Assignment 13
# Count Uppercase Letters
# ==========================================================

print("\nAssignment 13")
print("-" * 40)

# ---------- Solution ----------

with open("hello.txt", "r") as file:

    data = file.read()

count = 0

for ch in data:

    if ch.isupper():

        count += 1

print("Uppercase Letters :", count)


# ==========================================================
# Assignment 14
# Count Lowercase Letters
# ==========================================================

print("\nAssignment 14")
print("-" * 40)

# ---------- Solution ----------

with open("hello.txt", "r") as file:

    data = file.read()

count = 0

for ch in data:

    if ch.islower():

        count += 1

print("Lowercase Letters :", count)


# ==========================================================
# Assignment 15
# Find Longest Word
# ==========================================================

print("\nAssignment 15")
print("-" * 40)

# ---------- Solution ----------

with open("hello.txt", "r") as file:

    words = file.read().split()

print("Longest Word :", max(words, key=len))


# ==========================================================
# Assignment 16
# Find Shortest Word
# ==========================================================

print("\nAssignment 16")
print("-" * 40)

# ---------- Solution ----------

with open("hello.txt", "r") as file:

    words = file.read().split()

print("Shortest Word :", min(words, key=len))


# ==========================================================
# Assignment 17
# Replace One Word With Another
# ==========================================================

print("\nAssignment 17")
print("-" * 40)

# ---------- Solution ----------

old_word = input("Old Word : ")
new_word = input("New Word : ")

with open("hello.txt", "r") as file:

    data = file.read()

data = data.replace(old_word, new_word)

print("\nUpdated Content\n")
print(data)


# ==========================================================
# Assignment 18
# Create Uppercase Copy
# ==========================================================

print("\nAssignment 18")
print("-" * 40)

# ---------- Solution ----------

with open("hello.txt", "r") as source:

    data = source.read()

with open("uppercase.txt", "w") as destination:

    destination.write(data.upper())

print("Uppercase File Created")


# ==========================================================
# Assignment 19
# Create Lowercase Copy
# ==========================================================

print("\nAssignment 19")
print("-" * 40)

# ---------- Solution ----------

with open("hello.txt", "r") as source:

    data = source.read()

with open("lowercase.txt", "w") as destination:

    destination.write(data.lower())

print("Lowercase File Created")


# ==========================================================
# Assignment 20
# Complete File Analysis
# ==========================================================

print("\nAssignment 20")
print("-" * 40)

# ---------- Solution ----------

with open("hello.txt", "r") as file:

    data = file.read()

print("Characters :", len(data))
print("Words      :", len(data.split()))
print("Lines      :", len(data.splitlines()))

vowels = 0
digits = 0
uppercase = 0
lowercase = 0
spaces = 0
special = 0

for ch in data:

    if ch.lower() in "aeiou":

        vowels += 1

    if ch.isdigit():

        digits += 1

    if ch.isupper():

        uppercase += 1

    if ch.islower():

        lowercase += 1

    if ch == " ":

        spaces += 1

    if not ch.isalnum() and not ch.isspace():

        special += 1

print("Vowels     :", vowels)
print("Digits     :", digits)
print("Uppercase  :", uppercase)
print("Lowercase  :", lowercase)
print("Spaces     :", spaces)
print("Special Ch :", special)