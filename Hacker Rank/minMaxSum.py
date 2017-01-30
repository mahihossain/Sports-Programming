#!/usr/bin/python3

a,b,c,d,e = input().strip().split(' ')
a,b,c,d,e = [int(a),int(b),int(c),int(d),int(e)]

minSum = sum([a,b,c,d,e])-max(a,b,c,d,e)
maxSum = sum([a,b,c,d,e])-min(a,b,c,d,e)

print(str(minSum)+' '+str(maxSum))
