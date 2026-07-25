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