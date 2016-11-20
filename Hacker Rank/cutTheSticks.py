#!/usr/bin/python3

N = int(input().strip())
sticks = [int(a) for a in input().strip().split(' ')]
output = []

while len(sticks) != 0:
    minLen = min(sticks)
    sticks = [x-minLen for x in sticks]
    output.append(len(sticks))
    sticks = [x for x in sticks if x != 0]

for i in range(len(output)):
    print(output[i],end='\n')
