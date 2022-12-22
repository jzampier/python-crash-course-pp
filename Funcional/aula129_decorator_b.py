# """Continuing with decorators
# Signature of function = Name, parameters, return type
# """


# def speak_loudly(function):
#     """speak loudly function

#     Arguments:
#         function -- function parameter
#     """

#     def upper_case(*args):
#         """Put a given word in upper case

#         Arguments:
#             word -- string to upper case
#         """
#         return function(*args).upper()

#     return upper_case


# @speak_loudly
# def greet(word):
#     """Greets something

#     Arguments:
#         word -- Just a word to greet

#     Returns:
#         String
#     """
#     return f'Hello! {word}'

# @speak_loudly
# def order(ball_one, ball_two):
#     """Icecream

#     Arguments:
#         ball_one -- 1st flavor
#         ball_two -- 2nd flavor
#     """
#     return f"Hello, I'd like an icecream half {ball_one} and half {ball_two}!!!"

# @speak_loudly
# def message():
#     """Just a simple message
#     """
#     return 'Nice to meet you!!'

# print(greet("Good Morning!!!!!!"))
# print(order("Strawberry",'Chocolate'))
# print(message())

""""Case bellow = decorator with defined signature"""


def check_first_value(value):
    def inner(function):
        def original_function(*args):
            if args and args[0] != value:
                return f'Incorrect value. Fist arg must be {value}'
            return function(*args)

        return original_function

    return inner


@check_first_value(20)
def calculate(num_one, num_two):
    return num_one + num_two


print(calculate(20, 45))
print(calculate(10, 45))
