#!/usr/bin/python3

import math

t = int(input().strip())

for _ in range(t):
    a = [int(x) for x in input().strip().split(' ')]
    print(int(math.floor(math.sqrt(a[1]))) - int(math.ceil(math.sqrt(a[0])))+1)
