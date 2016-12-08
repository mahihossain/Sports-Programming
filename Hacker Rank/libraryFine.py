#!/usr/bin/python3

d1,m1,y1 = input().strip().split(' ')
d1,m1,y1 = [int(d1),int(m1),int(y1)]
d2,m2,y2 = input().strip().split(' ')
d2,m2,y2 = [int(d2),int(m2),int(y2)]

if d2<d1 and m2==m1 and y2==y1:
    print((d1-d2)*15)
elif m2<m1 and y2==y1:
    print((m1-m2)*500)
elif y1>y2:
    print("10000")
else:
    print("0")
