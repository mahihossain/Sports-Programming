#!/usr/bin/python3

n,d = [x for x in input().strip().split(' ')]
n,d = [int(n), int(d)]
c = [int(x) for x in input().strip().split(' ')]

counter = 0

for i in range(len(c)):
    if c[i]+d in c and c[i]+2*d in c:
        counter += 1

print(counter)
