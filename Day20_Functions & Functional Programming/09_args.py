def display_numbers(*args):
    print(args)
    print(type(args))
    for number in args:
        print(number)


display_numbers(10, 20, 30, 40)