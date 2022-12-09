"""Closure - A function is capable be aware of your surrounding
    Internal and external scope.
"""


def multiply(xvalue):
    def calculate(yvalue):
        return xvalue * yvalue

    return calculate


double : int = multiply(2)
triple : int = multiply(3)

print(f'O dobro de 4 eh {double(4)}')
print(f'O triplo de 5 eh {triple(5)}')

