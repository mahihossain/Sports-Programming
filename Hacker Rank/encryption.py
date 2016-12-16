#!/usr/bin/python3
import math

s = input().strip()
s = s.replace(' ','')
s1 = ''

for i in range(math.ceil(math.sqrt(len(s)))):
    j = i
    while j<=len(s)-1:
        s1 += s[j]
        j += math.ceil(math.sqrt(len(s)))

    if i != len(s)-1:
        s1 += ' '

print(s1)

