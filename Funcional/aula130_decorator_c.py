"""
Built-in Decorators

https://wiki.python.org/moin/PythonDecoratorLibrary

"""

#! 1
class House:
    def __init__(self, price) -> None:
        self.__price = price

    # def get_price(self):
    #     return self.price

    # def set_price(self, new_price):
    #     self.price = new_price
    @property  # *used to define the price
    def price(self):
        return self.__price

    @price.setter  # *used to set a new price
    def price(self, new_price):
        if new_price > 0 and isinstance(new_price, float):
            self.__price = new_price
        else:
            print('Type an valid value!')

    @price.deleter  # *used to delete price object
    def price(self):
        """
        Purpose:
        """
        del self.__price

    # end def


# my_house = House(450_000)
# print(my_house.price)

# my_house.price = 500_000
# print(my_house.price)

# #! 2

# my_house = House(450_000)
# print(my_house.get_price())

# my_house.set_price(500_000)
# print(my_house.get_price())
#! 3 Built-in decorators

my_house = House(450_000)
print(my_house.price)

my_house.price = 500_000.00
print(my_house.price)
