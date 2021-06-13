"""
Домашнее задание №1
Функции и структуры данных
"""
import math
def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [num ** 2 for num in numbers]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def is_prime(number):
    """
    функция принимает на вход число
    и показывает, простое ли оно
    >>> is_prime(5)
    <<< True
    >>> is_prime(6)
    <<< False
    """

    if number < 2:
        return False

    for i in range(2, round(math.sqrt(number))+1):
        if number % i == 0:
            return False
    return True

def is_odd(number):
    """
    функция принимает на вход число
    и показывает, нечетное ли оно
    >>> is_odd(1)
    <<< True
    >>> is_odd(2)
    <<< False
    """
    return True if number % 2 != 0 else False

def is_even(number):
    """
        функция принимает на вход число
        и показывает, четное ли оно
        >>> is_even(1)
        <<< False
        >>> is_even(2)
        <<< True
        """
    return True if number % 2 == 0 else False

filter_types = {ODD: is_odd, EVEN: is_even, PRIME: is_prime}

# Лучше строки вместо констант
# filter_types = {'ODD': is_odd, 'EVEN': is_even, 'PRIME': is_prime}

def filter_numbers(list_of_numbers, func_filter=ODD) :
    """
    функция, которая на вход принимает список из целых чисел
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    >>> filter_numbers([2, 3, 4, 5], PRIME)
    <<< [2, 3, 5]
    """

    return list(filter(filter_types[func_filter], list_of_numbers))

    # if func_filter == ODD:
    #     return list(filter(is_odd, list_of_numbers))
    # if func_filter == EVEN:
    #     return list(filter(is_even, list_of_numbers))
    # if func_filter == PRIME:
    #     return list(filter(is_prime, list_of_numbers))
