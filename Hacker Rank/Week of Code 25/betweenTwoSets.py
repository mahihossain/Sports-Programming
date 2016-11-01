#!/bin/python3

import sys


n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]
b = [int(b_temp) for b_temp in input().strip().split(' ')]

counter = 0
flag = False
#if min(b)%2 == 0:
    #numberList = [int(n) for n in range(2,min(b)+1,2)]
#else:
    #numberList = [int(n) for n in range(3,min(b)+1,2)]

numberList = [int(n) for n in range(1,min(b)+1)]

for i in numberList:
    if i >= max(a):
        for j in a:
            if i%j == 0:
                flag = True
                continue
            else:
                flag = False
                break
    else:
        continue



    if(flag):
        for k in b:
            if k%i == 0:
                flag = True
                continue
            else:
                flag = False
                break
    else:
        continue


    if(flag):
        counter += 1


print(counter)
        




