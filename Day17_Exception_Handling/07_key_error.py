employee = {
    "name": "Rahul",
    "salary": 50000
}

try:
    print(employee["age"])

except KeyError:
    print("The requested key does not exist")

print("Program completed")