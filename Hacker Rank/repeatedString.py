#!/usr/bin/python3

s = input().strip()
n = int(input().strip())

counter = s.count('a')*(int(n/len(s)))

remainder = n%len(s)

for i in range(remainder):
    if s[i] is 'a':
        counter += 1

print(counter)
