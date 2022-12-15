""" Challange, simmulating a for loop"""


def iter_name(strint_to_be_iterable: str):
    """simmulates a for loop to print each char of the name"""
    ite_name: iter = iter(strint_to_be_iterable)
    nbr_iterations: int = len(strint_to_be_iterable)
    i = 1
    while i <= (nbr_iterations):
        print(next(ite_name))
        i += 1


# ? OR
def my_loop(iterable: iter):
    """simmulates a for loop to print each char of an iterable"""
    an_iterable: iter = iter(iterable)
    while True:
        try:
            print(next(an_iterable), end=' ')
        except StopIteration:
            break
    print('')


NAME_TEST = 'Julio'
NUMBER_TEST = [1, 2, 3, 4, 5, 6, 7, 8, 9]
iter_name(NAME_TEST)
iter_name(NUMBER_TEST)
my_loop(NAME_TEST)
my_loop(NUMBER_TEST)
