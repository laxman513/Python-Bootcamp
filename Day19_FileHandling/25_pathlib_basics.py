from pathlib import Path

current_directory = Path.cwd()

file_path = Path("output.txt")

print("Current Directoy:")
print(current_directory)

print("\nFile Path:")
print(file_path)

print("\nDoes output.txt exist?:")
print(file_path.exists())