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
print(list_one)
print(sorted(touple_one))
