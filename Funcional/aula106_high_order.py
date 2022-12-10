"""Recebe / retorna uma funcao"""


def double(value):
    """sumary_line"""

    return value * 2


def square(value):
    """sumary_line"""

    return value * value


def calculate_function(operation, values, function):
    """ "sumary_line"""

    print(f'calculating operation: {operation}')
    for value in values:
        print(value, '->', function(value))


list_values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

calculate_function('double', range(1, 13), double)  #!passar a funcao sem ()
calculate_function('square', range(1, 13), square)  #!passar a funcao sem ()
