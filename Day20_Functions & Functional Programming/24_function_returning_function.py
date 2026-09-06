# Function returning another function

def create_multiplier(number):

    def multiplier(value):
        return value * number

    return multiplier


double = create_multiplier(2)
triple = create_multiplier(3)

print("Double:", double(10))
print("Triple:", triple(10))