with open("encoding_test.txt", "w", encoding="utf-8") as file:
    file.write("Python File Handling\n")
    file.write("Hello World\n")
    file.write("నమస్కారం\n")
    file.write("తెలుగు భాష\n")

with open("encoding_test.txt", "r", encoding="utf-8") as file:
    content = file.read()

print(content)