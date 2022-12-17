"""
Generators special functions that uses yield statement instead of return.
Spend less memory than regular function
yields an generator object that can be iterable with next()
"""


def counter(max_value: int):
    count = 1
    while count <= max_value:
        # ? yields the value of count and waits for next() to be executed
        yield count
        count += 1


gen = counter(5)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

print(next(gen))

#! Can be converted to a list, but it doesn't use the true potential of generators
def musical_notes():
    """yields a list of musical notes"""
    yield 'Dó'
    yield 'Ré'
    yield 'Mi'
    yield 'Fá'
    yield 'Sol'
    yield 'Lá'
    yield 'Si'


gen_two = musical_notes()
for note in gen_two:
    print(note)
