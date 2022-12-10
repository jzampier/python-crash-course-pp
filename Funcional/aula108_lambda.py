def double(xvalue):
    return xvalue * 2


print(double(4))
# assign to a variable
double2 = lambda value: value * 2
print(double2(4))
# using lambda straight into a function
print((lambda xvalue, yvalue, zvalue: xvalue + yvalue + zvalue)(1, 2, 3))


def greet():
    title = 'Mr/Ms'
    action = lambda something: title + ' ' + something
    return action


greetings = greet()
print(greetings('Harry Potter'))
