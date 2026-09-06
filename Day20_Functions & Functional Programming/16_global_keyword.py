value = 100


def test():
    global value

    value = 200

    print("Inside function:", value)


print("Before function:", value)

test()

print("After function:", value)