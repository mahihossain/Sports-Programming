#!/usr/bin/python3

n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
c = [int(x) for x in input().strip().split(' ')]
b = int(input())

c[k] = 0
if sum(c)/2 == b:
    print('Bon Appetit')
else:
    print(int(b-sum(c)/2))
