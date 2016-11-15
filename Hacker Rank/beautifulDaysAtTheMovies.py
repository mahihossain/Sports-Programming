#!/usr/bin/python3

i,j,k = input().strip().split(' ')
i,j,k = [int(i),int(j),int(k)]
counter = 0

for x in range(i,j+1):

    revI = int(str(x)[::-1])

    if abs(x-revI) % k == 0:
        counter += 1
    else:
        continue

print(counter)

