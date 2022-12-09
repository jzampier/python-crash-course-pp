# Property of call itself
""" Must have a break mechanism/condition. Otherwise function will be inan
    infinite loop
"""


def fatorial(value):
    """
    Purpose: Calculates the fatorial of a given value
    """
    return value * fatorial(value - 1) if value > 1 else 1


# end def
print(fatorial(5))
print(fatorial(10))
