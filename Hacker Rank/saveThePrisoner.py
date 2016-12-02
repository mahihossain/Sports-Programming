#!/usr/bin/python3

t = int(input().strip())

for _ in range(t):
    n,m,s = input().strip().split(' ')
    n,m,s = [int(n),int(m),int(s)]
    print((s-1+m-1)%n+1)
