"""Testing generators speed"""
import time


# def numbers(n: int):
#     """Generates sequencial numbers

#     Arguments:
#         n -- end

#     Yields:
#         number in sequence between 1 and n
#     """
#     for value in range(1, n):
#         yield value


# g_one = numbers(10)

# g_two = (value for value in range(1, 10))

# list_one = [nvalue for nvalue in range(1, 10)]

# print(g_one)
# print(g_two)
# print(list_one)

t_start = time.time()
gen = sum((num for num in range(1, 1_000_000)))
t_end = time.time()
time_generator = t_end - t_start

t_start = time.time()
liste = sum([num for num in range(1, 1_000_000)])
t_end = time.time()
time_liste = t_end - t_start

print(f'Time using generator -> {time_generator}\n', '-' * 70)
print(f'Time using List -> {time_liste}')
