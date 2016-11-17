#!/bin/python3

import sys


n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]

counter = 0

for i in range(len(a)):
    for j in range(len(a)):
        if i<j and (a[i] + a[j]) % k == 0:
            counter += 1
        else:
            continue

print(counter)
