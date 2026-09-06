# Nested function

def outer():

    def inner():
        print("Inside inner function")

    print("Inside outer function")

    inner()


outer()