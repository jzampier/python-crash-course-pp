"""all() and any()"""
list_one = [0, 1, 2, 3, 4, 5]
list_two = [1, 2, 3, 4, 5]
list_three = []
names = ['Petrucia', 'Repro', 'Paula', 'Piva', 'Pietra']

print("all(l1) ", all(list_one), "\n")
print("all(l2) ", all(list_two), "\n")
print("all(l3) ", all(list_three), "\n")

print("any(l1) ", any(list_one), "\n")
print("any(l2) ", any(list_two), "\n")
print("any(l3) ", any(list_three), "\n")

print(
    'All names start with "P" ? ',
    all(map(lambda elem: elem.startswith('P'), names)),
    '\n',
)
print(
    'Any name starts with "P" ? ',
    any(map(lambda elem: elem.startswith('P'), names)),
    '\n',
)
#!list compreencion name[0] is the first character of the name
print(all([name[0] == 'P' for name in names]))
