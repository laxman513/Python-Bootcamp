"""
==========================================================
Day 12 - File Handling
01_Programs.py
==========================================================
"""

# ==========================================================
# Program 1 - Open a File
# ==========================================================

print("\nProgram 1")
print("-" * 40)

file = open("sample.txt", "w")
print(type(file))

file.close()

# ==========================================================
# Program 2 - Write to a File
# ==========================================================

print("\nProgram 2")
print("-" * 40)

file = open("sample.txt", "w")
file.write("Hello Python")

file.close()

print("Data Written Successfully")

# ==========================================================
# Program 3 - Read Entire File
# ==========================================================

print("\nProgram 3")
print("-" * 40)

file = open("sample.txt", "r")

print(file.read())

file.close()

# ==========================================================
# Program 4 - Write Multiple Lines
# ==========================================================

print("\nProgram 4")
print("-" * 40)

file = open("student.txt", "w")

file.write("Laxman\n")
file.write("Darahas\n")
file.write("Dhanush\n")

file.close()

print("Student Data Written")

# ==========================================================
# Program 5 - Read One Line
# ==========================================================

print("\nProgram 5")
print("-" * 40)

file = open("student.txt", "r")

print(file.readline())

file.close()


# ==========================================================
# Program 6 - Read All Lines
# ==========================================================

print("\nProgram 6")
print("-" * 40)

file = open("student.txt", "r")

print(file.readlines())

file.close()


# ==========================================================
# Program 7 - Append Data
# ==========================================================

print("\nProgram 7")
print("-" * 40)

file = open("student.txt", "a")

file.write("Kiran\n")

file.close()

print("Data Appended Successfully")


# ==========================================================
# Program 8 - Read Updated File
# ==========================================================

print("\nProgram 8")
print("-" * 40)

file = open("student.txt", "r")

print(file.read())

file.close()


# ==========================================================
# Program 9 - Create New File Using x
# ==========================================================

print("\nProgram 9")
print("-" * 40)

try:

    file = open("newfile.txt", "x")

    file.write("Welcome")

    file.close()

    print("File Created")

except FileExistsError:

    print("File Already Exists")

# ==========================================================
# Program 10 - Use with Statement
# ==========================================================

print("\nProgram 10")
print("-" * 40)

with open("student.txt", "r") as file:

    print(file.read())

# ==========================================================
# Program 11 - Count Characters
# ==========================================================

print("\nProgram 11")
print("-" * 40)

with open("student.txt", "r") as file:
    data = file.read()

print("Characters:", len(data))

# ==========================================================
# Program 12 - Count Lines
# ==========================================================

print("\nProgram 12")
print("-" * 40)

with open("student.txt", "r") as file:
    lines = file.readlines()
print("Lines:", len(lines))

# ==========================================================
# Program 13 - Read File Line by Line
# ==========================================================

print("\nProgram 13")
print("-" * 40)

with open("student.txt", "r") as file:

    for line in file:

        print(line.strip())
    
# ==========================================================
# Program 14 - Check if File Exists
# ==========================================================

import os
print("\nProgram 14")
print("-" * 40)

if os.path.exists("student.txt"):
    print("File Exist")
else:
    print("File Not Found")

# ==========================================================
# Program 15 - Delete File
# ==========================================================

import os

print("\nProgram 15\n")
print("-" * 40)

if os.path.exists("newfile.txt"):
    os.remove("newfile.txt")
    print("File removed")
else:
    print("File Not Found")

# ==========================================================
# Program 16 - Read Character by Character
# ==========================================================

print("\nProgram 16")
print("-" * 40)

with open("student.txt", "r") as file:

    while True:

        ch = file.read(1)

        if ch == "":
            break

        print(ch)


# ==========================================================
# Program 17 - Count Number of Words
# ==========================================================

print("\nProgram 17")
print("-" * 40)

with open("student.txt", "r") as file:

    data = file.read()

words = data.split()

print("Total Words:", len(words))


# ==========================================================
# Program 18 - Count Number of Vowels
# ==========================================================

print("\nProgram 18")
print("-" * 40)

with open("student.txt", "r") as file:

    data = file.read()

count = 0

for ch in data.lower():

    if ch in "aeiou":

        count += 1

print("Total Vowels:", count)


# ==========================================================
# Program 19 - Search a Word
# ==========================================================

print("\nProgram 19")
print("-" * 40)

word = input("Enter word to search: ")

with open("student.txt", "r") as file:

    data = file.read()

if word in data:

    print("Word Found")

else:

    print("Word Not Found")


# ==========================================================
# Program 20 - Copy File
# ==========================================================

print("\nProgram 20")
print("-" * 40)

with open("student.txt", "r") as source:

    data = source.read()

with open("backup.txt", "w") as destination:

    destination.write(data)

print("File Copied Successfully")


# ==========================================================
# Program 21 - Count Number of Lines
# ==========================================================

print("\nProgram 21")
print("-" * 40)

with open("student.txt", "r") as file:

    count = 0

    for line in file:

        count += 1

print("Total Lines:", count)


# ==========================================================
# Program 22 - Count Occurrences of a Word
# ==========================================================

print("\nProgram 22")
print("-" * 40)

search = input("Enter word: ")

with open("student.txt", "r") as file:

    data = file.read()

print("Occurrences:", data.count(search))


# ==========================================================
# Program 23 - Find Longest Line
# ==========================================================

print("\nProgram 23")
print("-" * 40)

with open("student.txt", "r") as file:

    longest = ""

    for line in file:

        if len(line) > len(longest):

            longest = line

print("Longest Line:", longest.strip())


# ==========================================================
# Program 24 - Convert File to Uppercase
# ==========================================================

print("\nProgram 24")
print("-" * 40)

with open("student.txt", "r") as file:

    data = file.read()

print(data.upper())


# ==========================================================
# Program 25 - Print Even Numbered Lines
# ==========================================================

print("\nProgram 25")
print("-" * 40)

with open("student.txt", "r") as file:

    lines = file.readlines()

for i in range(len(lines)):

    if (i + 1) % 2 == 0:

        print(lines[i].strip())


# ==========================================================
# Program 26 - Merge Two Files
# ==========================================================

print("\nProgram 26")
print("-" * 40)

with open("file1.txt", "r") as file1:

    data1 = file1.read()

with open("file2.txt", "r") as file2:

    data2 = file2.read()

with open("merged.txt", "w") as file3:

    file3.write(data1)
    file3.write("\n")
    file3.write(data2)

print("Files Merged Successfully")


# ==========================================================
# Program 27 - Search Ignore Case
# ==========================================================

print("\nProgram 27")
print("-" * 40)

word = input("Enter word: ")

with open("student.txt", "r") as file:

    data = file.read()

if word.lower() in data.lower():

    print("Word Found")

else:

    print("Word Not Found")


# ==========================================================
# Program 28 - Replace Word
# ==========================================================

print("\nProgram 28")
print("-" * 40)

with open("student.txt", "r") as file:

    data = file.read()

old_word = input("Old Word : ")
new_word = input("New Word : ")

data = data.replace(old_word, new_word)

print("\nUpdated Content\n")
print(data)


# ==========================================================
# Program 29 - Count Digits
# ==========================================================

print("\nProgram 29")
print("-" * 40)

with open("student.txt", "r") as file:

    data = file.read()

count = 0

for ch in data:

    if ch.isdigit():

        count += 1

print("Digits:", count)


# ==========================================================
# Program 30 - Generate File Report
# ==========================================================

print("\nProgram 30")
print("-" * 40)

with open("student.txt", "r") as file:

    data = file.read()

print("Characters :", len(data))
print("Words      :", len(data.split()))
print("Lines      :", len(data.splitlines()))

# ==========================================================
# Program 31 - Count Uppercase Letters
# ==========================================================

print("\nProgram 31")
print("-" * 40)

with open("student.txt", "r") as file:

    data = file.read()

count = 0

for ch in data:

    if ch.isupper():

        count += 1

print("Uppercase Letters:", count)


# ==========================================================
# Program 32 - Count Lowercase Letters
# ==========================================================

print("\nProgram 32")
print("-" * 40)

with open("student.txt", "r") as file:

    data = file.read()

count = 0

for ch in data:

    if ch.islower():

        count += 1

print("Lowercase Letters:", count)


# ==========================================================
# Program 33 - Count Spaces
# ==========================================================

print("\nProgram 33")
print("-" * 40)

with open("student.txt", "r") as file:

    data = file.read()

print("Spaces:", data.count(" "))


# ==========================================================
# Program 34 - Reverse File Content
# ==========================================================

print("\nProgram 34")
print("-" * 40)

with open("student.txt", "r") as file:

    data = file.read()

print(data[::-1])


# ==========================================================
# Program 35 - Print File in Reverse Line Order
# ==========================================================

print("\nProgram 35")
print("-" * 40)

with open("student.txt", "r") as file:

    lines = file.readlines()

for line in reversed(lines):

    print(line.strip())


# ==========================================================
# Program 36 - Compare Two Files
# ==========================================================

print("\nProgram 36")
print("-" * 40)

with open("file1.txt", "r") as file1:

    data1 = file1.read()

with open("file2.txt", "r") as file2:

    data2 = file2.read()

if data1 == data2:

    print("Both Files Are Same")

else:

    print("Files Are Different")


# ==========================================================
# Program 37 - Remove Blank Lines
# ==========================================================

print("\nProgram 37")
print("-" * 40)

with open("student.txt", "r") as file:

    for line in file:

        if line.strip():

            print(line.strip())


# ==========================================================
# Program 38 - Remove Duplicate Lines
# ==========================================================

print("\nProgram 38")
print("-" * 40)

unique_lines = set()

with open("student.txt", "r") as file:

    for line in file:

        if line not in unique_lines:

            unique_lines.add(line)

            print(line.strip())


# ==========================================================
# Program 39 - Copy Only Non-Blank Lines
# ==========================================================

print("\nProgram 39")
print("-" * 40)

with open("student.txt", "r") as source, open("clean.txt", "w") as destination:

    for line in source:

        if line.strip():

            destination.write(line)

print("Clean File Created")


# ==========================================================
# Program 40 - Count Specific Character
# ==========================================================

print("\nProgram 40")
print("-" * 40)

character = input("Enter Character: ")

with open("student.txt", "r") as file:

    data = file.read()

print("Occurrences:", data.count(character))


# ==========================================================
# Program 41 - Find Longest Word
# ==========================================================

print("\nProgram 41")
print("-" * 40)

with open("student.txt", "r") as file:

    words = file.read().split()

longest = max(words, key=len)

print("Longest Word:", longest)


# ==========================================================
# Program 42 - Find Shortest Word
# ==========================================================

print("\nProgram 42")
print("-" * 40)

with open("student.txt", "r") as file:

    words = file.read().split()

shortest = min(words, key=len)

print("Shortest Word:", shortest)


# ==========================================================
# Program 43 - Create Uppercase Copy
# ==========================================================

print("\nProgram 43")
print("-" * 40)

with open("student.txt", "r") as source:

    data = source.read()

with open("uppercase.txt", "w") as destination:

    destination.write(data.upper())

print("Uppercase File Created")


# ==========================================================
# Program 44 - Create Lowercase Copy
# ==========================================================

print("\nProgram 44")
print("-" * 40)

with open("student.txt", "r") as source:

    data = source.read()

with open("lowercase.txt", "w") as destination:

    destination.write(data.lower())

print("Lowercase File Created")


# ==========================================================
# Program 45 - Word Frequency Counter
# ==========================================================

print("\nProgram 45")
print("-" * 40)

with open("student.txt", "r") as file:

    words = file.read().lower().split()

frequency = {}

for word in words:

    frequency[word] = frequency.get(word, 0) + 1

for word, count in frequency.items():

    print(f"{word} : {count}")


# ==========================================================
# Program 46 - Count Total Digits
# ==========================================================

print("\nProgram 46")
print("-" * 40)

with open("student.txt", "r") as file:

    data = file.read()

count = 0

for ch in data:

    if ch.isdigit():

        count += 1

print("Total Digits:", count)


# ==========================================================
# Program 47 - Count Special Characters
# ==========================================================

print("\nProgram 47")
print("-" * 40)

with open("student.txt", "r") as file:

    data = file.read()

count = 0

for ch in data:

    if not ch.isalnum() and not ch.isspace():

        count += 1

print("Special Characters:", count)


# ==========================================================
# Program 48 - Count Alphabets
# ==========================================================

print("\nProgram 48")
print("-" * 40)

with open("student.txt", "r") as file:

    data = file.read()

count = 0

for ch in data:

    if ch.isalpha():

        count += 1

print("Alphabets:", count)


# ==========================================================
# Program 49 - Display Line Numbers
# ==========================================================

print("\nProgram 49")
print("-" * 40)

with open("student.txt", "r") as file:

    for index, line in enumerate(file, start=1):

        print(index, ":", line.strip())


# ==========================================================
# Program 50 - Backup File
# ==========================================================

print("\nProgram 50")
print("-" * 40)

with open("student.txt", "r") as source:

    data = source.read()

with open("student_backup.txt", "w") as backup:

    backup.write(data)

print("Backup Created Successfully")


# ==========================================================
# Program 51 - Read First 20 Characters
# ==========================================================

print("\nProgram 51")
print("-" * 40)

with open("student.txt", "r") as file:

    print(file.read(20))


# ==========================================================
# Program 52 - Read Last Line
# ==========================================================

print("\nProgram 52")
print("-" * 40)

with open("student.txt", "r") as file:

    lines = file.readlines()

print("Last Line:", lines[-1].strip())


# ==========================================================
# Program 53 - Count Empty Lines
# ==========================================================

print("\nProgram 53")
print("-" * 40)

count = 0

with open("student.txt", "r") as file:

    for line in file:

        if line.strip() == "":

            count += 1

print("Empty Lines:", count)


# ==========================================================
# Program 54 - Sort Words Alphabetically
# ==========================================================

print("\nProgram 54")
print("-" * 40)

with open("student.txt", "r") as file:

    words = file.read().split()

words.sort()

for word in words:

    print(word)


# ==========================================================
# Program 55 - Remove Leading and Trailing Spaces
# ==========================================================

print("\nProgram 55")
print("-" * 40)

with open("student.txt", "r") as file:

    for line in file:

        print(line.strip())


# ==========================================================
# Program 56 - Print Only Numeric Values
# ==========================================================

print("\nProgram 56")
print("-" * 40)

with open("student.txt", "r") as file:

    data = file.read().split()

for item in data:

    if item.isdigit():

        print(item)


# ==========================================================
# Program 57 - Reverse Every Line
# ==========================================================

print("\nProgram 57")
print("-" * 40)

with open("student.txt", "r") as file:

    for line in file:

        print(line.strip()[::-1])


# ==========================================================
# Program 58 - Create Numbered File
# ==========================================================

print("\nProgram 58")
print("-" * 40)

with open("student.txt", "r") as source, open("numbered.txt", "w") as destination:

    line_no = 1

    for line in source:

        destination.write(f"{line_no}. {line}")

        line_no += 1

print("Numbered File Created")


# ==========================================================
# Program 59 - Find File Size
# ==========================================================

import os

print("\nProgram 59")
print("-" * 40)

size = os.path.getsize("student.txt")

print("File Size:", size, "bytes")


# ==========================================================
# Program 60 - Complete File Analysis
# ==========================================================

print("\nProgram 60")
print("-" * 40)

with open("student.txt", "r") as file:

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