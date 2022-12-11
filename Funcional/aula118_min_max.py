"""Functions min() and max()"""
list_one = [1, 45, 78, 9, 34, 67, 23]
touple_one = (3, 56, 3, 56, 23, 1)
PHRASE_ONE = 'Uncle Julio is amazing'
names = ['Adriana', 'Ronny', 'Rene', 'Marcelo', 'Tereza']
songs = [
    {'title': 'Amigo', 'played': 4},
    {'title': 'Ai se eu te pego', 'played': 45},
    {'title': 'Para sempre', 'played': 12},
    {'title': 'Nuvem de lagrimas', 'played': 23},
    {'title': 'Papel Mache', 'played': 14},
]

print(
    f'Lowest value of list_one is {min(list_one)}, Greatest value of list_one is {max(list_one)}',
    '\n',
    '-' * 50,
)
print(
    f'Lowest value of touple_one is {min(touple_one)}, Greatest value of touple_one is {max(touple_one)}',
    '\n',
    '-' * 50,
)
print(
    f'Lowest value of PHRASE_ONE is < {min(PHRASE_ONE)} >, Greatest value of PHRASE_ONE is < {max(PHRASE_ONE)} >',
    '\n',
    '-' * 50,
)

print(max(names, key=lambda name: len(name)))

print(min(names, key=lambda name: len(name)))

print(min(songs, key=lambda song: song.get('played')), '\n', "-" * 50)
print(max(songs, key=lambda song: song.get('played')), '\n', "-" * 50)
