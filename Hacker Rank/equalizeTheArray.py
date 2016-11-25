#!/usr/bin/python3

input()
array = [int(x) for x in input().strip().split(' ')]
 
count = 0
numCounter = {}
 
for number in array:
    if number in numCounter:
        numCounter[number] += 1
    else:
        numCounter[number] = 1
 
sortedList = sorted(numCounter, key = numCounter.get, reverse = True)
 
for i in array:
    if i != sortedList[0]:
        count += 1
    else:
        continue

print(count)
