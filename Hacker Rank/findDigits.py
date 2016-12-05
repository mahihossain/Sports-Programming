#!/usr/bin/python3

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    count = 0
    temp = n
    while temp != 0:
        digit = temp%10
        if digit != 0 and n%digit == 0:
            count += 1
        temp = int(temp/10) 
    print(count)
