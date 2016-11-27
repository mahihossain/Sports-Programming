#!/usr/bin/python3

import string

h = [int(h_temp) for h_temp in input().strip().split(' ')]
word = input().strip()

maxH = 0
alpha = list(string.ascii_lowercase)

for i in word:
    if h[alpha.index(i)] > maxH:
        maxH = h[alpha.index(i)]
    else:
        continue

print(len(word)*maxH)
