import sys, os

TYPE_ERROR_TEXT = 'Args should be int or float'


class User:
    def __init__(self, name, surname, age):
        self.name = name + ' ' + surname
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age}"

    @classmethod
    def is_user_adult(cls, user):
        if user.age >= 18:
            return True
        else:
            return False

    @classmethod
    def is_user_elderly(cls, user):
        if user.age > 65:
            return True
        else:
            return False


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


print(Solver.add(1, 2))
print(type(None))
