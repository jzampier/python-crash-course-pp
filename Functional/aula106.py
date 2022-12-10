"""High Order Functions

Functions that are able to receive and return other functions

"""


def double(x_value):
    """double(x_value)

    Arguments:
        x_value -- input integer or float

    Returns:
        double of x_value
    """
    return x_value * 2


def square(x_value):
    """power of x_value

    Arguments:
        x_value -- integer or float

    Returns:
        x_value times x_value
    """
    return x_value * x_value


def calculate(operation, lista, function):
    """Calculates the given operation for each element of the list

    Arguments:
        operation -- str explaining the operation
        lista -- array of numbers
        function -- disired operation function
    """
    print(f"Calculating: {operation}")
    for y_value in lista:
        print(y_value, '->', function(y_value))


calculate('Double of 1 to 6', range(1, 6), double)
calculate('Square of 1 to 6', range(1, 6), square)
