# Recursion example

def countdown(number):

    if number == 0:
        return

    print(number)

    # Recursive call
    countdown(number -1)

countdown(5)

