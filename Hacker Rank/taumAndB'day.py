#!/usr/bin/python3

t = int(input().strip())

for _ in range(t):
    b,w = input().strip().split()
    b,w = [int(b),int(w)]
    x,y,z = input().strip().split()
    x,y,z = [int(x),int(y),int(z)]

    if x>y and x>(z+y):
        print(y*w + (y+z)*b)
    elif y>x and y>(z+x):
        print(x*b + (x+z)*w)
    else:
        print(x*b + y*w)

