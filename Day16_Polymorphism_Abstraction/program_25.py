# Program 25 - Functions as Arguments
def square(x):
    return x * x

def cube(x):
    return x * x * x

def calculate(operation, number):
    return operation(number)

print(calculate(square, 5))
print(calculate(cube, 5))
