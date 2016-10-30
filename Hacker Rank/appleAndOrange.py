#!/bin/python3

import sys

appleCounter = orangeCounter = 0

s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]

for i in range(len(apple)):
    apple[i] += a

for i in range(len(orange)):
    orange[i] += b

for i in apple:
    if i >= s and i<= t:
        appleCounter += 1
    else:
        pass

for i in orange:
    if i >= s and i<=t:
        orangeCounter += 1
    else:
        pass

print(appleCounter)
print(orangeCounter)
