print('====Anonymous function**Lambda**=======')

'''
* Lambda arguments:Expression
* Function can have any number of arguments but only one expression
'''
'''
Normal function
def cube(num):
    return num * num * num

print(cube(3))
'''

result = (lambda num: num * num* num)(3)
print(result)

# or

cube = lambda num :num * num *num
print(cube(3))