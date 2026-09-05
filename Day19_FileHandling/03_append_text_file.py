file = open("output.txt", "a")

file.write("This line was added using append mode.\n")
file.write("The original content was preserved.\n")

file.close()