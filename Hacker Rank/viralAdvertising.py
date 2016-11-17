#!/usr/bin/python3

people = 5
like = 0

for i in range(int(input())):
    people = int(people/2)
    like += people
    people *= 3

print(like)
