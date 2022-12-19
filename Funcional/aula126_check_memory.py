"""Check memory usage with generators"""
from sys import getsizeof

# def fibo_list(end):
#     fibo = []
#     fibo = [0, 1]
#     for i in range(2, end + 1):
#         y = fibo[i - 1] + fibo[i - 2]
#         fibo.append(y)
#     return fibo


def fibo_list(end):
    fibo = []
    a, b = 0, 1
    fibo.append(0)
    while len(fibo) < end:
        fibo.append(b)
        a, b = b, a + b
    return fibo


print(fibo_list(14))


# def fibonacci_of(n):
#     if n in {0, 1}:  # Base case
#         return n
#     return fibonacci_of(n - 1) + fibonacci_of(n - 2)
# for i in range(14):
#     print(fibonacci_of(i))
def fibo_gen(max_value: int):
    a, b, count = 0, 1, 0
    while count < max_value - 1:
        # ? yields the value of count and waits for next() to be executed
        a, b = b, a + b
        yield a
        count += 1


fibo_one = fibo_gen(14)
list_fibos = [0]
for fibo in fibo_one:
    list_fibos.append(fibo)

print(list_fibos)


lista_fibo_list = fibo_list(10000)
lista_fibo_gen = fibo_gen(10000)

print(
    f'Generator = {getsizeof(lista_fibo_gen)} ;;; Lista = {getsizeof(lista_fibo_list)} '
)
