"""Filter, applies a function that returns True or False to an iterable.
    each element that returned True is included in the filter object (result of
    filter function).
    You can also convert the result into an list
"""

import statistics

#! filter(function,iterable)
true_list1 = list(filter(lambda x: x > 3, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(true_list1, '\n')

true_list2 = filter(lambda char: char > 'j', 'Julio Zampier1201/1!')
print(list(true_list2), '\n')
#                                   number % 2 = 0 (false)
true_list3 = filter(lambda number: number % 2, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(true_list3), '\n')

# On dictionaries
list_dict = [
    {'name': 'Jose', 'age': 28},
    {'name': 'Adriana', 'age': 39},
    {'name': 'Pedro', 'age': 17},
    {'name': 'Maria', 'age': 23},
    {'name': 'Roberto', 'age': 15},
]

# !Iterable : list_dict
# ?Item : each dictionary insideh st_dict

less_eighteen = list(filter(lambda item: item.get('age') < 18, list_dict))
print('less than eighteen ->', less_eighteen, '\n')

more_five_chars = list(filter(lambda item: len(item.get('name')) > 5, list_dict))
only_names = list(map(lambda item: item.get('name'), more_five_chars))
print('more than five chars ->', more_five_chars, '\n')
print('more than five chars (just names) ->', only_names, '\n')

# Ahead of the curve
data = [1.2, 3.4, 1.7, 4.5, 3.2, 2.3, 5.6, 2.4, 1.6]
mean = statistics.mean(data)

ahead_of_the_curve = list(filter(lambda value: value > mean, data))
ahead_of_the_curve.sort()
print(f'Mean = {mean}\n')
print('Ahead of the curve ->', ahead_of_the_curve, '\n')


cities = ['', 'São Paulo', 'Itu', '', 'Bauru', 'Jundiaí', '', 'Sorocaba']
# ? empty strings '' = False, we can use it to filter empty values
filtered_cities = list(filter(None, cities))
print('Filtered by none ->', filtered_cities, '\n')
