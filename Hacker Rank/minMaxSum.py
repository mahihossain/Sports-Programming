#!/usr/bin/python3

x = [int(y) for y in input().strip().split(' ')]

minSum = sum(x)-max(x)
maxSum = sum(x)-min(x)

print(str(minSum)+' '+str(maxSum))
