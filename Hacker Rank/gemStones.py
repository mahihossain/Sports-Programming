#!/usr/bin/python3
import string,re

n = int(input().strip())
strings = []
d = dict.fromkeys(string.ascii_lowercase, 0)
counter = 0

for i in range(n):
    strings.append(input().strip())

for i in strings:
    while i != '':
        j = 0
        d[i[j]] += 1
        i = re.sub(i[j],'',i)
        j += 1

for i in d.values():
    if i == n:
        counter += 1
    else:
        continue

print(counter)



