print('===============SET=====================')
# Un orderd collection
#set doesn't accept mutable element'
anchors = {'annaya', 'raj', 'pradeep', 'arvid','pradeep'}

print(type(anchors))
empty_set = set()
print(len(empty_set))
print(anchors)
anchors.add('sushanth')
print(anchors)
anchors.update(['jul', 'rit', 'vic'])
print(anchors)

anchors.discard('raj')
print(anchors)
#anchors.remove('annaya')
print(anchors)
anchors.discard('Tulsi')
#anchors.remove('tulsi')
anchors.update(['jul', 'rit', 'vic'])
#print(anchors.pop())
#anchors.clear()
print('=====================***************=================')
print(anchors)
print(anchors.pop())
print(anchors)

print('==========union============')
a = {10, 20, 30, 40}
b = {53, 45, 85, 69, 20}

abUnion = a.union(b)
#abUnion = a | b
print(abUnion)
#abIntersection = a.intersection(b)
abIntersection = a & b
print(abIntersection)

# difference == a -b set of elements that are only in a but not in b
abDifference = a.difference(b)
#abDifference = a - b
print(abDifference)

#Symmetric difference
abSymmetric = a ^ b
#abSymmetric = a.symmetric(b)
print(abSymmetric)

print('==================== Dictionary========================')

bioData = {'name': 'sushanth', 'address': 'skdfskd', 'subscribe': True}

print(type(bioData))

information = {'1':'sushanth', '2':{1:'sush',2:bioData}}
print(information)
#print(information['2'])
print(information.get('2'))
'''
D1 ={12: {'class': 'b.com fy', 'percentage': 78.70},
    15: {'class': 'b.com fy', 'percentage': 88.70},
     }
rollNumber = int(input('Enter your roll number'))

percentage = D1[rollNumber]['percentage']
if(percentage > 40):
    print('passed')
else:
    print('failed')


'''


information['1'] = 'sush'
print(information)
information['vic']= 'myson'
print(information)