# Function as an argument

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def caluculation(operation, a, b):
    return operation(a, b)


result1 = caluculation(add, 3, 4)

result2 = caluculation(multiply, 3, 4)

print("Result1:", result1)

print("Result2:", result2)


