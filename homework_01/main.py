"""
Домашнее задание №1
Функции и структуры данных
"""
def power_numbers(*numbers):
    """
    функция, которая принимает N целых чисел,
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

    if number < 2:
        return False

    # for i in range(2, math.floor(math.sqrt(number))):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def filter_numbers(list_of_numbers: list [int], func_filter) :
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if func_filter == ODD:
        return list(filter(lambda num: True if num % 2 != 0 else False, list_of_numbers))
    if func_filter == EVEN:
        return list(filter(lambda num: True if num % 2 == 0 else False, list_of_numbers))
    if func_filter == PRIME:
        return list(filter(is_prime, list_of_numbers))
