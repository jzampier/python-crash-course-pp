"""Reduce, applies a function wich receives at least two arguments and applies 
    the function to the remaining arguments.
    reduce(function, optional initial sequence[]) returns value
    x + y = z, z becomes new x , next array becomes y and then x + y again.
    #!from functools import reduce
"""

from functools import reduce

list_one = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
people = [
    {'name': 'Joao', 'age': 28},
    {'name': 'Carla', 'age': 16},
    {'name': 'Jose', 'age': 50},
    {'name': 'Adriana', 'age': 23},
    {'name': 'Ronny', 'age': 14},
]

reduce_one = reduce(lambda x, y: x + y, list_one)
print(reduce_one, "\n")
# *          reduce(lambda x, y: x + y, list    , initial value)
reduce_two = reduce(lambda x, y: x + y, list_one, 100)
print(reduce_two, "\n")
# ?Example bellow does not work
# reduce_three = reduce(lambda x, y: x + y, 100, list_one)
# print(reduce_three, "\n")
#!fatorial = lambda n: reduce(lambda x, y: x * y, range(1,n+1))
fatorial = lambda n: reduce(lambda x, y: x * y, range(1, n + 1))
print(fatorial(5), "\n")

# get all ages
ages = map(lambda p: p.get('age'), people)

# filter by ages lower than 18
f_ages = filter(lambda age: age < 18, ages)

# reduce
sum_less_eighteen_alt = reduce(lambda x, y: x + y, f_ages)
print(sum_less_eighteen_alt, "\n")

# * Or
sum_less_eighteen = reduce(
    lambda x, y: x + y,
    map(
        lambda item: item.get('age'),
        filter(lambda item: item.get('age') < 18, people),
    ),
)
print(sum_less_eighteen, "\n")
