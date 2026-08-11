# Day 15 - Program 13
# Encapsulation, properties, validation and property inheritance.
#
# This numbered file corresponds to Program 13 from the Day 15 learning sequence.
# The complete reference implementation and mini-project are in mini_project.py.

class Example:
    def __init__(self, value):
        self.__value = value

    @property
    def value(self):
        return self.__value

example = Example(13)
print(example.value)
