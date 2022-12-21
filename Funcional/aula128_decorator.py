""""
Decorator extends the functionality of a function improving or changing its
behavior. Uses sugar syntax @
"""


def be_polite(function):
    def being():
        print('Hello!')
        function()
        print('Nice to meet you!')

    return being

@be_polite
def greet():
    print('Be welcome to the world!')

greet()
