#!/usr/bin/python3

input()
socks = [x for x in input().strip().split(' ')]
counter = 0

for i in socks:
    temp = socks.count(i)
    counter += int(temp/2)
    socks = [x for x in socks if x != i]

print(counter)
               
