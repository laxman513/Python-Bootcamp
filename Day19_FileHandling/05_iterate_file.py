file = open("output.txt", "r")

for line in file:
     print(line, end="")

file.close()