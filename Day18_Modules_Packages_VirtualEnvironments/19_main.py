from utils.calculator import add, multiply
from utils.validator import is_positive, is_valid_age

print("Addition:", add(10, 20))
print("Multiplication:", multiply(5, 4))

print("Is 10 positive?", is_positive(10))
print("Is age 25 valid?", is_valid_age(25))