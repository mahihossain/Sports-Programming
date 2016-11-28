#!/usr/bin/python3
'''This code is not most optimized, methods were used to show the method
usablity.

Since python is general purpose language it is always possible to avoid any
specific way when problem solving'''

input()
a = [int(x) for x in input().strip().split(' ')]
b = [int(x) for x in input().strip().split(' ')]

maxA = max(a)
minB = min(b)
numbers = [int(x) for x in range(max(b)+1) if x >= maxA and x <= minB]

'''This method takes an integer and a list and return boolean depending on if
all the elements of the list is a factor of x'''

def isFactor(x,l):
    flag = True
    for i in l:
        if x % i == 0:
            continue
        else:
            flag = False
            break

    return flag

'''This method takes an integer and a list and return boolean depending on if
x is a factor of all the elements of the list'''

def ofFactor(x,l):
    flag = True
    for i in l:
        if i % x == 0:
            continue
        else:
            flag = False
            break

    return flag

'''It is really not necessary to rearrange the list according to what is
wanted on the problem a simple counter would be enough'''

for i in numbers:
    numbers = [x for x in numbers if isFactor(x,a) and ofFactor(x,b)]

print(len(numbers))

    
