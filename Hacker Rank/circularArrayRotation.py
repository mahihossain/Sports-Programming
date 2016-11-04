#!/bin/python3

import sys,collections


n,k,q = input().strip().split(' ')
n,k,q = [int(n),int(k),int(q)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]

d = collections.deque(a)
d.rotate(k)
for i in range(len(d)):
    a[i] = d[i]

for a0 in range(q):
    m = int(input().strip())
    print (a[m])
