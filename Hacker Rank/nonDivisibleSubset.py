#!/usr/bin/python3

n,k = [int(x) for x in input().strip().split(' ')]
n,k = [int(n),int(k)]
numbers = [int(x) for x in input().strip().split(' ')]

counts = [0] * k
for number in numbers:
    counts[number % k] += 1

count = min(counts[0], 1)
for i in range(1, k//2+1):
    if i != k - i:
        count += max(counts[i], counts[k-i])
if k % 2 == 0: 
    count += 1

print (count)


