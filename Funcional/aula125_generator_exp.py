"""
Generator expressions
! gen = (i**2 for i in range(10) if i % 2 == 0)
"""

import sys

# gen = (i**2 for i in range(10) if i % 2 == 0)
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#! Generator expression
gen = (i**2 for i in range(10000) if i % 2 == 0)
#! List comprehenssion
lc = [i**2 for i in range(10000) if i % 2 == 0]

print(f'Gen = {sys.getsizeof(gen)}')
print(f'LC = {sys.getsizeof(lc)}')
