import sys, os

TYPE_ERROR_TEXT = 'Args should be int or float'


class Solver:

    @classmethod
    def add(cls, a, b):
        if all(map(lambda x: isinstance(x, (int, float)), (a, b))):
            result = a + b
        else:
            raise TypeError(TYPE_ERROR_TEXT)
        return result

    @classmethod
    def remove_file(cls, filepath):
        if os.path.isfile(filepath):
            os.remove(filepath)


class User:
    def __init__(self, name, surname, age):
        self.name = name + ' ' + surname
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age}"


print(Solver.add(1, 2))
print(type(None))


