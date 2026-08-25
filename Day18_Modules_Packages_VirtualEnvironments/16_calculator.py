def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def main():

    print("Calculator Application")

    result1 = add(10, 20)
    result2 = subtract(20, 5)

    print("Addition:", result1)
    print("Subtraction:", result2)


if __name__ == "__main__":
    main()