"""Create a function that behaves like the range() function"""


class Counter:
    """counter function"""

    def __init__(self, start: int, end: int):
        """
        Purpose: simmulates a range() function
        """
        self.start = start
        self.end = end

    #!Redefine __iter__ and __next__
    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self.start < self.end:
            num = self.start
            self.start += 1
            return num
        else:
            raise StopIteration


# numbers = Counter(1, 5)
# iterable = iter(numbers)
for i in Counter(1, 11):
    print(i)
