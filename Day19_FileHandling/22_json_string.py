import json

student = {
    "name": "Rahul",
    "age": 20,
    "marks": 85
}

# Python dictionary → JSON string
json_string = json.dumps(student)

print("JSON String:")
print(json_string)

# JSON string → Python dictionary
python_data = json.loads(json_string)

print("\nPython Dictionary:")
print(python_data)

print("\nStudent Name:", python_data["name"])