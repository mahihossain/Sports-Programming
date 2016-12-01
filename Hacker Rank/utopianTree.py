#!/usr/bin/python3

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    size = 1
    for i in range(1,n+1):
        if i % 2 == 0:
            size += 1 
        else:
            size += size

    print(size)
