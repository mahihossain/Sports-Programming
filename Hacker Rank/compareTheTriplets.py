#!/bin/python3

import sys


a0,a1,a2 = input().strip().split(' ')
alice = a0,a1,a2 = [int(a0),int(a1),int(a2)]
b0,b1,b2 = input().strip().split(' ')
bob = b0,b1,b2 = [int(b0),int(b1),int(b2)]

aliceCounter = 0
bobCounter = 0

for i in range(3):
    if(alice[i] > bob[i]):
        aliceCounter += 1
    elif(bob[i] > alice[i]):
        bobCounter += 1
    else:
        pass
    

print(str(aliceCounter)+ ' ' +str(bobCounter))

