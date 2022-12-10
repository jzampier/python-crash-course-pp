"""Lazy Evaluation - Delays processing until the last moment."""


def square(xvalue):
    """Calculates value times value

    Keyword arguments:
    xvlaue -- value (int)
    Return: value * value
    """
    return lambda: xvalue * xvalue


functions = [square(i) for i in [1, 2, 3, 4, 5]]
for function in functions:
    print(function())
