from pathlib import Path

current_folder = Path.cwd()

print("Current folder:")
print(current_folder)

print("\nFiles and folders:")

for item in current_folder.iterdir():
    print(item)