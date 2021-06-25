print('========>control flow<=================')

lastball = 1
'''
if lastball == 6:
    print('Won the match ')
else:
    print('Lost the match')
'''
print('won the match') if lastball ==6 else print('lost the match') # shorthand
'''
# program to check wheather a number is even or odd
number = int(input('Enter a number:'))

if number % 2 == 0:
    print('It is number is even')
else:
    print('it is odd number')
'''
'''
# Nested if

number = int(input('Enter a number: '))
if number % 2 == 0:
    if number % 4 == 0:
        print('Congrats, this number is divided by  both 2 and 4 ')
    else:
        print('sorry')
else:
    print('sorry this number is not divided by 2 or 4')
'''
'''
# if-elif ladder: btech admissions

rank = int(input('Enter your rank:'))
if rank <= 1000:
    print('you got college 1')
elif rank > 1000 and rank <= 10000:
    print('You got college2')
elif rank > 10000 and rank <= 40000:
    print('You got college 3')
else:
    print('sorry, for your rank, no college available')
'''
'''
x = 10

if x < 20 : print('greater')
'''
'''
print('=========FOR LOOP===============')
numbersList = [1, 2, 45, 25, 65 , 47 ]
for number in numbersList:
    print(number *5)

name = 'sushanth'
for char in name:
    print(char)
 '''
'''
for num in range(100, 0, -1):
    print(num)
'''
'''
name = input('Enter your name:')
print(name[-2:])
lastTwoCharacters = name[-2:]
for num in range(1, 11):
    print(lastTwoCharacters * num)
'''
'''
numbers = {1:'one', 2:'two', 3:'three'}
for num in numbers:
    print(num)
    print(numbers[num])
'''
'''
name = input('Enter your name:')
vowelsList = ['a', 'e', 'i', 'o', 'u']

for char in name:
    if char in vowelsList:
        print(char, '-it is in vowel')
    else:
        print(char, '-it is consonant')

'''
'''
name = input('Enter your name:')
vowelsList = ['a', 'e', 'i', 'o', 'u']
for char in name:
    if char in vowelsList:
        print(char, '-Found vowel')
        break
'''
'''
# print the sum of marks
marks = [20, 52, 56, 85, 45]
sum = 0
for mark in marks:
    sum = sum + mark
print('Total sum:', sum)

'''
'''
print('============WHILE loop=================')
i = 1
while i <= 10:
    print(i)
    i += 1
'''
import random

print(random.randint(1, 31))
score = 0
scoreInfo = []
while score < 500:
    scoreValue = random.randint(1, 31)
    score = score+scoreValue
    scoreInfo.append(scoreValue)
print('Total Flips:', len(scoreInfo))
print(scoreInfo, score)

