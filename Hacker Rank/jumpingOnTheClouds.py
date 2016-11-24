#!/usr/bin/python3

n = int(input().strip())
c = [int(x) for x in input().strip().split(' ')]

counter = 0
c.insert(n,0)
i=0

while (i<n-1):
    i+= (c[i+2] == 0)+1
    counter += 1

print(counter)
