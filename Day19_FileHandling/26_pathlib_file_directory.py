from pathlib import Path

file_path = Path("output.txt")

directory_path = Path(".")

print("FILE CHECK")

print("Exists:", file_path.exists())
print("Is File:", file_path.is_file())
print("Is Directory:", file_path.is_dir())

print("\nDIRECTORY CHECK")
print("Exists:", directory_path.exists())
print("Is File:", directory_path.is_file())
print("Is Directory:", directory_path.is_dir())
