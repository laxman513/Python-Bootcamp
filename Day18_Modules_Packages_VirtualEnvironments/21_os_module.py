import os

print("Current directory:")
print(os.getcwd())

print("\nFiles and folders:")
for item in os.listdir():
    print(item)