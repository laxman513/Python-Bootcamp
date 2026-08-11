# Program 02 - Common Function with Different Objects
class Dog:
    def sound(self):
        print("Woof")

class Cat:
    def sound(self):
        print("Meow")

def make_sound(animal):
    animal.sound()

make_sound(Dog())
make_sound(Cat())
