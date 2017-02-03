#!/usr/bin/python3

p = int(input().strip())
q = int(input().strip())
s = ''

for i in range(p,q+1):
    r = i**2
    a = ''
    b = ''
    l = list(str(r))
    sLen = len(l) - len(str(i))

    for j in range(sLen,len(l)):
        a += l[j]

    for k in range(sLen):
        b += l[k]

    if a == '':
        a = 0
    if b == '':
        b = 0

    if int(a)+int(b) == i:
        s += str(i)
        if i != q:
            s += ' '

if s != '':
    print(s)
else:
    print('INVALID RANGE')
    

        
 
        
