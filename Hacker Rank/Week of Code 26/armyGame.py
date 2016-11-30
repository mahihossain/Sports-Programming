#!/usr/bin/python3

n,m = input().strip().split(' ')
n,m = [int(n),int(m)]

print((int(m/2) + m%2) * (int(n/2) + n%2))
