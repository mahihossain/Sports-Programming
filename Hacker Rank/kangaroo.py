#!/usr/bin/python3

import sys


x1,v1,x2,v2 = input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]

startPoint = 0

if(x1>x2):
    startPoint = x2
else:
    startPoint = x1

flag = False
numX1 = x1
numX2 = x2


for _ in range(startPoint,10001):
    numX1 += v1
    numX2 += v2

    if((numX1 - numX2)==0):
        flag = True
        break
    else:
        continue

if flag:
    print('YES')
else:
    print('NO')

    
