"""Inverts any iterable returning a reversed object without change the original object"""
list_one = [1, 2, 3, 4, 5, 6, 7]

lr = list(reversed(list_one))
tr = tuple(reversed(list_one))

print(f'lr -> {lr}, \ntr -> {tr}\n')

PHRASE = 'Uncle Julio is the best'

for char in reversed(PHRASE):
    #! end='' changes \n to ''
    print(char, end='')
print('\n')

#! Another way
print(f'Another way -> {PHRASE[::-1]}')
