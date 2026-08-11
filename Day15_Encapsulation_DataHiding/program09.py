# Day 15 - Program 09
# Encapsulation, properties, validation and property inheritance.
#
# This numbered file corresponds to Program 09 from the Day 15 learning sequence.
# The complete reference implementation and mini-project are in mini_project.py.

class Example:
    def __init__(self, value):
        self.__value = value

    @property
    def value(self):
        return self.__value

example = Example(9)
print(example.value)
