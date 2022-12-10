"""Sorts an iterable preserving all original values

Keyword arguments:
argument -- any iterable
Return: a list

#! Important: This function is not the same as sort() method, that applies only
#! to lists and returns and returns the original list changed.

"""
list_one = [3, 5, 1, 8, 4, 2]
touple_one = (3, 5, 1, 8, 4, 2)

list_one.sort()
print(list_one, '\n', "-" * 20)

#! If we don't assign it to a variable, it will be consumed on print
print(sorted(touple_one), '\n', "-" * 20)
print(sorted(touple_one, reverse=True), '\n', "-" * 20)

songs = [
    {'title': 'Amigo', 'played': 4},
    {'title': 'Ai se eu te pego', 'played': 45},
    {'title': 'Para sempre', 'played': 12},
    {'title': 'Nuvem de lagrimas', 'played': 23},
    {'title': 'Papel Mache', 'played': 14},
]
most_played_songs = sorted(songs, key=lambda song: song.get('played'), reverse=True)
print(most_played_songs, '\n', "-" * 20)
