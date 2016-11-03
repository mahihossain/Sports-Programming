#!/bin/python3

import sys


s = input().strip()
t = input().strip()
k = int(input().strip())

length = 0
size = 0

if len(s) > len(t) and s[0] == t[0]:
    length = len(t)
    for i in range(length):
        if s[i] == t[i]:
            continue
        else:
            break
    size = (len(s)-(i)) + (len(t)-(i))

    if k == size:
        print('Yes')
    elif k > size and k%2 == 0:
        print('Yes')
    else:
        print('No')


elif len(t)>len(s) and s[0] == t[0]:
    length = len(s)
    for i in range(length):
        if s[i] == t[i]:
            continue
        else:
            break

    size = (len(s)-(i)) + (len(t)-(i))

    if k == size:
        print('Yes')
    elif k > size and k%2 == 0:
        print('Yes')
    else:
        print('No')

    


elif s == t:
    if k%2==0 and k>=2:
        print('Yes')
    elif k%2 is not 0 and k > len(t):
        print('Yes')
    else:
        print('No')




elif s is not t:
    if len(s) + len(t) < k:
        print('Yes')
    else:
        print('No')
    


