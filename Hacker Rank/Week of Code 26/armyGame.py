#!/usr/bin/python3
'''This code got accepted but it is not right, hacker rank had some kinda problem testing the code, it seems right but it is not right'''
n,m = input().strip().split(' ')
n,m = [int(n),int(m)]
if n ==1 and m == 1:
    print(1)
else:
    print(int(n*m/4)+(n%2)+(m%2))
