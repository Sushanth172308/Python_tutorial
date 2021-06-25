from functools import reduce
print('====filter, map, reduce====')
# all of these takes a function and list
# Takes a function and iterable and creates a filtered list based on given condition

# filter(function,iterable)

def isEven(num):
    return num % 2 == 0

numbers = [10, 11, 23, 80, 87]
result = filter(isEven, numbers)# numbers is iterable list here
print(list(result))

# filtering using anonymous function insted of isEven

numbers = [10, 11, 23, 80, 87]
result = filter(lambda num: num % 2 == 0, numbers)

print(list(result))


# MAP
def capitableLetter(name):
    return name.upper()

friends = ['jenney', 'marry', 'loggy']
result = map(capitableLetter, friends)
print(list(result))

friends = ['jenney', 'marry', 'loggy']
result = map(lambda name: name.upper(), friends)
print(list(result))

# Reduce(function , sequence , initial)  here initial is optional
# *Returns single value

def addAll(a, b):
    return a + b

numbers = [20, 1, 3 , 10, 5]
result = reduce(addAll, numbers)
print(result)
numbers = [20, 1, 3 , 10, 5]
result = reduce(addAll, numbers, 10)
print(result)

numbers = [20, 1, 3 , 10, 5]

result = reduce(lambda a, b: a +b, numbers, 20)
print(result)


