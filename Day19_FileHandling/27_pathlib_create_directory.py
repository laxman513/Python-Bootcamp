from pathlib import Path

data_directory = Path("data")

data_directory.mkdir(exist_ok=True)

print("Data directory created or already exists.")
print("Directory exists:", data_directory.exists())
print("Is directory:", data_directory.is_dir())


path = Path("data") / "students.csv"

print(path)
print(path.exists())
print(path.resolve())