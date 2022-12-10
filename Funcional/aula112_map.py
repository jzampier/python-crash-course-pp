import math

"""Map function
    Apply a function to each element of an iterable and returns a list
    Eg:
        map(function or none, [1, 2, 3]) -> result : [1, 2, 3]
"""
lista = [1, 2, 3, 4, 5]
lista_two = [11, 12, 13, 14, 15]
lista_three = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

phrase = map(str, lista)

# *save in a variable and convert it to a list, otherwise you will consume these data
lphrase = list(phrase)
print('map', lphrase, '\n')
#####################################
# *with lambda function
#! lambda parameter: return
# ? lambda    par   : par*2 + par
new_list = list(map(lambda par: par * par * par, lista))
print('map with lambda function', new_list, '\n')

# * Also map function can be applied to multiples iterables, but map function
# * will group by element's position
# * Eg: map(function, [1, 2, 3],[4, 5, 6])
# * returns [(1,4), (2,5), (3,6)]
# Same lengths (desired)
soma = map(lambda x, y: x + y, lista, lista_two)
list_soma = list(soma)
print('l1 + l2 ->', list_soma, '\n')

# In this case lists have different lengths
soma2 = map(lambda x, y: x + y, lista, lista_three)
list_soma2 = list(soma2)
print('l1+l3 ->', list_soma2, '\n')

#
la = [1, 3, 5]
lb = [2, 4, 6]
lx = [0, 0, 0]
#                keep this order 1, 2, 3              1 , 2 , 3
list_lin_coef = list(map((lambda a, b, x: a * x + b), la, lb, lx))
print(list_lin_coef, '\n')
# calculates the area of each giver ray
list_ray = [3.4, 1.2, 11.3, 2.5, 5]
list_areas = list(map((lambda ray: math.pi * ray**2), list_ray))
print(f'Areas -> {list_areas}', '\n')

# Price adjust
products = [('tv', 2500), ('fogao', 1240), ('radio', 234)]
ADJUST = 1 + 10 / 100
# lambda prod: (prod[0], prod[1] * adjust)
adjusted_products = list(
    map(lambda product: (product[0], product[1] * ADJUST), products)
)
print(adjusted_products, '\n')

# On dictionaries
list_dict = [
    {'name': 'Jose', 'age': 28},
    {'name': 'Adriana', 'age': 39},
    {'name': 'Pedro', 'age': 50},
    {'name': 'Maria', 'age': 23},
]

# !Iterable : list_dict
# ?Item : each dictionary inside list_dict

# name = lambda item: item.get('name')
# age = lambda item: item.get('age')
# agesum = sum(map(age))

only_names: list = list(map(lambda item: item.get('name'), list_dict))
print('Names ->', only_names, '\n')

only_ages: list = list(map(lambda item: item.get('age'), list_dict))
print("Ages ->", only_ages, '\n')
print('Sum of all Ages ->', sum(only_ages), '\n')
