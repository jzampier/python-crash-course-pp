"""Iterable and Iterator"""

#!Iterable
# ?Returns an iterator when you run the function iter()

name = 'Uncle Julio'
numbers = [1, 2, 3, 4, 5]

# *Iterator
it_name = iter(name)
it_numbers = iter(numbers)

print(next(it_numbers))
print(next(it_numbers))

print(f'\n{next(it_name)}')
print(next(it_name))
print(next(it_name))
print(next(it_name))
print(next(it_name))
print(next(it_name))
print(next(it_name))
print(next(it_name))
print(next(it_name))
print(next(it_name))
print(next(it_name))

#! Challange, simmulating a for loop
name_two = 'Julio'


def iter_name(strint_to_be_iterable: str):
    """simmulates a for loop to print each char of the name"""
    ite_name: iter = iter(strint_to_be_iterable)
    nbr_iterations: int = len(strint_to_be_iterable)
    i = 1
    while i <= (nbr_iterations):
        print(next(ite_name))
        i += 1


iter_name(name_two)
