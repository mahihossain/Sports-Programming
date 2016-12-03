#!/usr/bin/python3

n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
c = [int(x) for x in input().strip().split(' ')]

energy = 100
i = -1

while i != 0:
    if i == -1:
        i += 1
    i = (i+k)%n
    if c[i] == 0:
        energy -= 1
    else:
        energy -= 3

print(energy)
