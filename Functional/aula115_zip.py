l1 = [1, 2, 3, 4, 5]
l2 = [11, 12, 13, 14, 15]
t1 = (11, 12, 13, 14, 15)
d1 = {'a': 21, 'b': 22, 'c': 23, 'd': 24}
result = zip(l1, l2)
print(list(result))

result2 = zip(l1, t1, d1.values())
print(list(result2))

v1 = [1200, 234, 2345, 1560]
v2 = [1245, 300, 2103, 1434]
p = ['fogao', 'liquidificador', 'geladeira', 'tv']
#!            product :      greatest_sale
list_comp = {venda[0]: max(venda[1], venda[2]) for venda in zip(p, v1, v2)}
print(list_comp)