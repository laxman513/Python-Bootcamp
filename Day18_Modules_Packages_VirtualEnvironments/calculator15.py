def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


print("Calculator module loaded")

if __name__ == "__main__":
    print("Running calculator directly")

    print("Addition:", add(10, 20))
    print("Subtraction:", subtract(20, 5))