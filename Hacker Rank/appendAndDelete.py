#!/usr/bin/python3

s = input().strip()
t = input().strip()
k = int(input().strip())

c = 0
f = 0

while c < min(len(s),len(t)) and s[c] == t[c]:
    c += 1

if k%2 == (len(s)+len(t)) %2 :
    f = len(s) + len(t) - c*2
else:
    f = len(s) + len(t) + 1

if k < f:
    print('No')
else:
    print('Yes')
    
