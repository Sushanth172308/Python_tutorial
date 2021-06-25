# Data types
# 1 . Numeric(int, float , complex
#improt cmath

marks = 500

percentage = (marks/600) * 100
print('Percentage:', percentage)
x = 5 + 10j
y = 12 + 8j
print(type(x))
print(x.real)
print(x.imag)
print(x.conjugate())
print(x +y)


# 2 . Sequence

# string
myName = '''sushanth'''
statement = '''sushanth is learning python 
            program , please get an encourage mentwhat a greate how are you'''
print(myName)
print(statement, len(statement))

# accessing a char in string --> indexing & slicing

language = "Python language" + "Python is awesome" * 4
print(language)



print('Accessing Elements from string:')
print(language[0])
language = 'sushanth'

print(language[::-1])
print(language[-2])

print(language[-1:-5:-1])

# Member ship
name = 'victor,rita and julia are brother and sisters'
print('julia' in name)
print('hello' not in name)


# Lists

print('==============LIST======================')

marks = [50, 20, 90, 65, 98, 98, 'sushanth']
print(marks)
disliker = []
print(len(disliker))
friends = ['Mark', 'Funka', 'Judy']
print('count of friends:', friends)

bioDataList = [27, '99556561', 'address', friends]
print(bioDataList)
print('Second friends in the list', friends[1])
print('Nested list friends:', bioDataList[3][0])
marks[1] = 55
print(marks)

marks_friends = marks + friends *2
print(marks_friends)
marks.append(100)
print(marks)
friends.extend(['tom', 'raj', 'king'])
print(friends)
friends.insert(1, 'Amal')
print('-----Inserting multiple values at a  specific position----------')
print(friends)
friends[1:1] = ['ads', 'sdfd', 'sdfsd']
print(friends)

del friends[1]
print(friends)
friends.remove('sdfd')
print(friends)

friends.pop(1)
print(friends)


print('----------------TUPLE----------------------------------')

marks = 20, 50, 80, 87, 26, [12, 25, 3]
print(type(marks))
marks1 = ('20',)
print(type(marks1))
friends ='Mark', 'sdfsd', 'Amal', 'Funka', 'Judy', 'tom', 'raj', 'king'
print(friends)
print(marks[1])
#print(friends[-2.0])
marks[-1][0] = 33
print(marks)


print('-----boolearn----')

subscribe = True
print(type(subscribe))

followed = False
print(type(followed))

a = 100
b = 100
c = 0

print(type(a == b))
print(bool(a))
print(bool(c))
