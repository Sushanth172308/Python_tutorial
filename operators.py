# operators

from datetime import date
a = 7
b = 10

print('Addition :', a +b )
print('Subtraction:', a-b)
print('Multiplication', a *b)

# Relational Operators:

a = 9

b = 2

print(a == b)
print(a >b)
print(a<b)
print(a >= b)
print(a!= b)

yearOfbirth = input('please enter your year of birth: ')
currentYear = date.today().year

age = currentYear - int(yearOfbirth)
print('Your age is:', age)